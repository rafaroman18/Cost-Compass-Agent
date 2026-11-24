from sentence_transformers import SentenceTransformer
from pypdf import PdfReader
import json
import numpy as np
import time

def create_embeddings(chunks_path: str):
    """
    Creates a vector embeddings (embeddings.npy file) from the chunks file provided. 

    Params:

        chunks_path: The path of the .jsonl chunks file
    """

    chunks = []

    # Extracting the text from the chunks
    with open(chunks_path, "r") as f:

        # Inserting the chunks into a list
        for l in f.read().split('\n'):
            if l != '':
                chunks.append(json.loads(l))

        # Extracting the text from every chunk
        texts = [c["chunk"] for c in chunks] 

    if not texts:
        print('An error occurred during the execution of this script. No text was extracted from the chunks.')
        return
    else:
        print(f'Success! {len(texts)} sentences been extracted from the chunks.')

    # Creating the embeddings model
    emb_model = SentenceTransformer("BAAI/bge-m3")

    # Creating embeddings in groups, so we can print the progress
    batch_size = 500
    all_embeddings = []
    start_total = time.perf_counter()
    
    for start in range(0, len(texts), batch_size):
    
        start_batch = time.perf_counter()
    
        batch = texts[start:start + batch_size]
        all_embeddings.append(emb_model.encode(batch, batch_size=64))
    
        done = min(start + batch_size, len(texts))
        print(f'{done}/{len(texts)} chunks ({done / len(texts):.0%}) - '
              f'this group: {time.perf_counter() - start_batch:.1f}s - '
              f'total: {time.perf_counter() - start_total:.1f}s')
    
    embeddings = np.vstack(all_embeddings)

    # Saving the embeddings
    np.save("Steps/Step 4 - RAG Benchmark/embeddings.npy", embeddings)

    print('Embeddings created!')

if __name__ == "__main__":
    create_embeddings("Steps/Step 4 - RAG Benchmark/chunks.jsonl")