import numpy as np

class Naive_Retrieval:

    embeddings = None
    chunks = []

    def __init__(self):
        self.embedding = np.load('Steps/Step 4 - RAG Benchmark/embeddings.npy')