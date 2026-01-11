import json
from sentence_transformers import SentenceTransformer
import faiss
import numpy as np

# Load embedding model (local & free)
embedding_model = SentenceTransformer("all-MiniLM-L6-v2")

# Load knowledge base
with open("knowledge_base.json", "r") as f:
    kb = json.load(f)

# Convert KB to text chunks
documents = []

for plan, details in kb["pricing"].items():
    documents.append(f"{plan.capitalize()} plan details: {details}")

for policy, text in kb["policies"].items():
    documents.append(f"Policy - {policy}: {text}")

# Create embeddings
embeddings = embedding_model.encode(documents, convert_to_numpy=True)

# Build FAISS index
dimension = embeddings.shape[1]
index = faiss.IndexFlatL2(dimension)
index.add(embeddings)

def answer_with_rag(query: str, top_k: int = 2) -> str:
    """
    Retrieves relevant context from the knowledge base
    and returns a grounded answer.
    """
    query_embedding = embedding_model.encode([query], convert_to_numpy=True)
    distances, indices = index.search(query_embedding, top_k)

    retrieved_docs = [documents[i] for i in indices[0]]

    return " | ".join(retrieved_docs)
