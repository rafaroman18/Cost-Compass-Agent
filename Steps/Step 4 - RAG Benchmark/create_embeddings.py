from sentence_transformers import SentenceTransformer
from pypdf import PdfReader
import json
import numpy as np

def create_embeddings():

    chunks = []

    # Extracting the text from the chunks
    with open("Steps/Step 4 - RAG Benchmark/chunks/chunks.jsonl", "r") as f:

        # Inserting the chunks into a list
        for l in f.read().split('\n'):
            if l != '':
                chunks.append(json.loads(l))

        # Extracting the text from every chunk
        texts = [c["chunk"] for c in chunks] 

    if texts is None:
        print('An error occurred during the execution of this script. No text was extracted from the chunks.')
        return
    else:
        print(f'Success! {len(texts)} sentences been extracted from the chunks.')

    # Creating the embeddings model
    emb_model = SentenceTransformer("BAAI/bge-m3")

    # Creating embeddings
    embeddings = emb_model.encode(texts)

    # Saving the embeddings
    np.save("embeddings.npy")

    print('Embeddings created!')

if __name__ == "__main__":
    create_embeddings()