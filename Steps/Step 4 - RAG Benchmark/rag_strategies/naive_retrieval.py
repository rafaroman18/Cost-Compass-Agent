from sentence_transformers import SentenceTransformer
from numpy import dot, load, argsort, flip
from numpy.linalg import norm
import json


class Naive_Retriever:


    def __init__(self):

        # Initializing embeddings.npy
        self.embeddings = load('Steps/Step 4 - RAG Benchmark/embeddings.npy')

        # Initializing chunks
        self.chunks = []
        with open("Steps/Step 4 - RAG Benchmark/chunks.jsonl", "r") as f:
            # Inserting the chunks into a list
            for l in f.read().split('\n'):
                if l != '':
                    self.chunks.append(json.loads(l))

        # Initializing the embeddings model
        self.model_bge3 = SentenceTransformer("BAAI/bge-m3")


    def retrieve(self, user_prompt: str, k=5):
        """
        Retrieves the k chunks most similar to the user question using the Naive Strategy.

        Params:

            user_prompt: The user question or petition.
            k: The number of chunks to return.

        Returns:

            list[dict]: The k most similar chunks (text, page, file, block), sorted from most to least similar.
        """

        # Convert the user prompt into a vector
        prompt_vec = self.model_bge3.encode(user_prompt)

        # Check the cosine similarity between the prompt and the chunks
        cos_sim = self.__cosine_similarity(self.embeddings, prompt_vec)

        # Take the indexes of the k most similar chunks
        k_idx = flip(argsort(cos_sim)[-k:])

        # Retrieve the chunks 
        return [self.chunks[id] for id in k_idx]

    
    def __cosine_similarity(self, a: list, b: list):
        """
        Cosine similarity between two matrices.

        Params:
            a: first matrix
            b: second matrix

        Returns:
            list/int: cosine similarity
        """
        return dot(a, b)/(norm(a)*norm(b))
