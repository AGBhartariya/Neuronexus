# core/memory_store.py

import os
import numpy as np
import google.generativeai as genai
from dotenv import load_dotenv
from sklearn.metrics.pairwise import cosine_similarity

# Load API key
load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

class MemoryStore:
    def __init__(self):
        self.embeddings = []
        self.data = []

    def get_embedding(self, text: str):
        # Use Gemini embedding model
        response = genai.embed_content(
            model="models/embedding-001",
            content=text,
            task_type="retrieval_document"
        )
        return np.array(response['embedding'], dtype=np.float32)

    def add_memory(self, text):
        embedding = self.get_embedding(text)
        self.embeddings.append(embedding)
        self.data.append(text)

    def search(self, query, top_k=3):
        if not self.embeddings:
            return []

        query_embedding = self.get_embedding(query).reshape(1, -1)
        all_embeddings = np.array(self.embeddings)
        similarities = cosine_similarity(query_embedding, all_embeddings)[0]
        top_indices = similarities.argsort()[::-1][:top_k]

        return [self.data[i] for i in top_indices]
