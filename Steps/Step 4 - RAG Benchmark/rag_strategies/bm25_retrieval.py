import json
from rank_bm25 import BM25Okapi
import nltk
from nltk.stem import SnowballStemmer
from nltk.corpus import stopwords
import re

nltk.download('punkt_tab')
nltk.download('stopwords')

class BM25_Retriever:


    def __init__(self):
        # Setting stop_words
        self.stop_words = set(stopwords.words('spanish'))
        
        # Initializing chunks and texts from chunks
        self.chunks = []
        self.texts = []
        with open("Steps/Step 4 - RAG Benchmark/chunks.jsonl", "r", encoding="utf-8") as f:
            # Inserting the chunks into a list
            for l in f.read().split('\n'):
                if l != '':
                    cur_chunk = json.loads(l)

                    # Storing the chunks
                    self.chunks.append(cur_chunk)

                    # Preprocess and stores the chunk's text
                    self.texts.append(self.__preprocess_text(cur_chunk['chunk']))

        # Generating bm25 indexes
        self.bm25 = BM25Okapi(self.texts)

    def retrieve(self, user_prompt: str, k=5):
        """
        Retrieves the k chunks that best match the user question using the BM25 Strategy.

        Params:

            user_prompt: The user question or petition.
            k: The number of chunks to return.

        Returns:

            list[dict]: The k best-scoring chunks (text, page, file, block), sorted from highest to lowest BM25 score.
        """

        # Tokenizing the user prompt 
        prompt_tok = self.__preprocess_text(user_prompt)

        # Retrieve the K most similar chunks
        return self.bm25.get_top_n(prompt_tok, self.chunks, k)
    
    def __preprocess_text(self, text: str):
        """
        Preprocess the text applying these techniques:
            - Removing punctuation and lowering text
            - Tokenization
            - Stemming
            - Removing Stop Words

        Params:
            text: Provided text

        Return:
            str: the preprocessed text
        """

        # Removing punctuation, lowering text and tokenization
        low = re.findall(r"\d+(?:[./,]\d+)*|[^\W\d_]+", text.lower())

        # Removing Stop Words
        removed = [word for word in low if word.lower() not in self.stop_words]

        # Stemming
        stemmer = SnowballStemmer("spanish")
        stemmed = [stemmer.stem(word) for word in removed]

        return stemmed