from sentence_transformers import SentenceTransformer
from pypdf import PdfReader
import re
from pathlib import Path
import numpy as np
import torch
import json

model = SentenceTransformer("BAAI/bge-m3")
tokenizer = model.tokenizer


# Lines that appear in every page of some pdfs (headers, footers...)
NOISE_LINES = [
    r"BOLETÍN OFICIAL DEL ESTADO",
    r"LEGISLACIÓN CONSOLIDADA",
    r"Página \d+",
    r".*\(\d+/\d+\)",
    r"Instituto N\s?acional de Estadística",
]


def process_all_pdfs(data_path: str = "Steps/Step 1 - Data and domain"):
    """
    This function will process every report pdf of the Step 1 folder (Housing, Employment, Energy and Prices).
    Each pdf generates its own chunks file in the chunks folder.

    Params:

        data_path: The path of the Step 1 folder

    Returns:

        int: The total number of chunks generated
    """

    total_chunks = 0
    all_chunks = []

    # Every pdf inside <block>/Reports/
    pdf_paths = sorted(Path(data_path).glob("*/Reports/*.pdf"))

    for i, pdf_path in enumerate(pdf_paths, start=1):

        # The block is the folder that contains Reports (Housing, Employment...)
        chunks = process_pdfs(str(pdf_path), pdf_path.parent.parent.name)
        total_chunks += len(chunks)
        all_chunks.extend(chunks)

        print(f"[{i}/{len(pdf_paths)}] {pdf_path.name}: {len(chunks)} chunks")

    # We will append all chunks into one big file also
    with open(f"Steps/Step 4 - RAG Benchmark/chunks/chunks.jsonl", "w", encoding="utf-8") as f:
        for chunk in all_chunks:
            f.write(json.dumps(chunk, ensure_ascii=False) + "\n")

    return total_chunks

def process_pdfs(pdf_path: str, block: str):
    """
    This function will process one pdf: it splits it into pages, cleans every page and splits it into chunks.

    Params:

        pdf_path: The path of the pdf file
        block: The block of the pdf (Housing, Employment, Energy or Prices)

    Returns:

        list[dict]: Every chunk of the pdf and metadata (page, file, block)
    """

    chunks = []
    file_name = Path(pdf_path).name

    # Looping through every page (the first page is 1)
    for page_number, page in enumerate(PdfReader(pdf_path).pages, start=1):

        text = clean_pdfs(page.extract_text() or "")

        chunks += split_page_in_chunks(text, page_number, file_name, block)

    # Saving the chunks into a .jsonl file (one chunk per line)
    with open(f"Steps/Step 4 - RAG Benchmark/chunks/chunks_{file_name}.jsonl", "w", encoding="utf-8") as f:
        for chunk in chunks:
            f.write(json.dumps(chunk, ensure_ascii=False) + "\n")

    return chunks


def clean_pdfs(page_text: str):
    """
    This function will clean the text of a pdf page (repeated headers, footers, bullet symbols...).

    Params:

        page_text: The text extracted from the page of the pdf

    Returns:

        str: The page text without the noise
    """

    lines = []

    # Looping through every line of the page
    for line in page_text.split("\n"):

        # Removing the lines that only contain a header or a footer
        if any(re.fullmatch(pattern, line.strip()) for pattern in NOISE_LINES):
            continue

        lines.append(line)

    text = "\n".join(lines)

    # Removing the private use symbols (bullets of the pdf font)
    text = re.sub(r"[\ue000-\uf8ff]", " ", text)

    return text

def split_page_in_chunks(page_text: str, page_number: int, file_name: str, block: str, n_tokens=400, overlap_tokens=50):
    """
    This function will split the received text from a pdf page into chunks of at most n_tokens tokens.

    Params:

        page_text: The text extracted from the page of the pdf
        page_number: The number of the page in the pdf
        file_name: The name of the pdf file
        block: The block of the pdf (Housing, Employment, Energy or Prices)
        n_tokens: The maximum number of tokens of each chunk
        overlap_tokens: The number of tokens repeated at the start of the next chunk

    Returns:

        list[dict]: Every chunk and metadata (page, file, block)
    """

    chunks, cur_chunk = [], []
    token_counter = 0

    # Removing every line break or similar
    text = " ".join(page_text.split())

    # Splitting into every sentence
    sentences = re.split(r'(?<=[.!?])\s+(?=[A-ZÁÉÍÓÚÑ¿¡])', text)

    # Looping through every sentence
    for i, s in enumerate(sentences):

        sentence_tokens = count_tokens(s)

        # If the current chunk plus the sentence is too long,
        # we will inserted the current chunk if there is one stored.
        # Else, we will split the sentence.
        if token_counter + sentence_tokens > n_tokens:

            # If a chunk is already stored, we inserted it
            # in the final list
            if len(cur_chunk) > 0:

                # Insert the generated chunk
                chunks.append({'chunk': " ".join(cur_chunk), 'page': page_number, 'file': file_name, 'block': block})

                # Resetting current chunk and counter and inserting overlapping chunks
                cur_chunk, token_counter  = overlap_chunk(cur_chunk, overlap_tokens)

            if sentence_tokens > n_tokens:

                # Splitting sentence
                # We will keep the last chunk for the next iteration (saving it in cur_chunk)
                chunks_to_store, cur_chunk, token_counter = split_long_sentences(s, n_tokens, overlap_tokens)

                # Inserting the generated chunks in the long sentence
                for c in chunks_to_store:
                    chunks.append({'chunk': c, 'page': page_number, 'file': file_name, 'block': block})

                continue

            # If the overlap plus the sentence does not fit, we discard the overlap
            if token_counter + sentence_tokens > n_tokens:
                cur_chunk, token_counter = [], 0

        # If the sentence is too short, we take that sentence
        # and we will check if the next sentence fits in it too.
        cur_chunk.append(s)

        # Adding the number of tokens
        token_counter += sentence_tokens

    # Inserting the last chunk that is still open
    if len(cur_chunk) > 0:
        chunks.append({'chunk': " ".join(cur_chunk), 'page': page_number, 'file': file_name, 'block': block})

    return chunks

def split_long_sentences(sentence: str, n_tokens: int, overlap_tokens: int):
    """
    This function will split a sentence longer than n_tokens into chunks of n_tokens tokens.

    Params:

        sentence: The sentence to split
        n_tokens: The maximum number of tokens of each chunk
        overlap_tokens: The number of tokens repeated between two consecutive chunks

    Returns:

        list[str]: Every complete chunk, except the last one
        str: The last chunk, kept to continue it in the next iteration
        int: The number of tokens of the last chunk
    """

    chunks = []
    step = n_tokens - overlap_tokens
    start = 0

    ids = tokenizer.encode(sentence, add_special_tokens=False)

    # We select the complete chunks
    while(start < len(ids) - step):

        # Saving the chunk
        chunks.append(tokenizer.decode(ids[start:start+n_tokens]))

        # Moving the start one step
        start += step

    # We will use the last chunk for the next iteration
    cur_chunk = [tokenizer.decode(ids[start:start+n_tokens])]
    token_counter = len(ids[start:start+n_tokens])

    return chunks, cur_chunk, token_counter


def overlap_chunk(cur_chunk: list, overlap_tokens: int):
    """
    This function will take the last sentences of a closed chunk that fit in overlap_tokens tokens.

    Params:

        cur_chunk: The sentences of the chunk that has just been closed
        overlap_tokens: The maximum number of tokens of the overlap

    Returns:

        list[str]: The sentences that will start the next chunk
        int: The number of tokens of those sentences
    """

    overlap = []
    tokens = 0

    # Looping from the last sentence to the first one
    for sentence in reversed(cur_chunk):

        sentence_tokens = count_tokens(sentence)

        # Stop when the next sentence does not fit in the overlap
        if tokens + sentence_tokens > overlap_tokens:
            break

        # Keeping the original order of the sentences
        overlap.insert(0, sentence)
        tokens += sentence_tokens

    return overlap, tokens
        

def count_tokens(text: str):
    """
    This functions counts the number of tokens of a string using the tokenizer in BAAI/bge-m3 model.

    Params:
        text: string to check the tokens

    Returns:
        int: the number of tokens
    """
    return len(tokenizer.encode(text, add_special_tokens=False))


if __name__ == "__main__":
    process_all_pdfs()
