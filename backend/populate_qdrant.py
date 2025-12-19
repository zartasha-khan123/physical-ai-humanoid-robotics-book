# populate_qdrant.py
import os
from qdrant_client import QdrantClient
from openai import OpenAI
from dotenv import load_dotenv
from retriving import RAGRetriever

load_dotenv()

# Initialize Qdrant
qdrant_client = QdrantClient(
    url=os.getenv("QDRANT_URL"),
    api_key=os.getenv("QDRANT_API_KEY")
)

# Initialize OpenAI
openai = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# Collection name
collection_name = "rag_embedding"

# Example documents
docs = [
    {"id": 1, "content": "ROS 2 is a robotics framework used for building robots.", "source": "test_doc.md"},
    {"id": 2, "content": "Humanoid robots can use ROS 2 for communication, control, and sensors.", "source": "test_doc.md"}
]

points = []
for doc in docs:
    embedding = openai.embeddings.create(
        model="text-embedding-ada-002",
        input=doc["content"]
    ).data[0].embedding
    points.append({
        "id": doc["id"],
        "vector": embedding,
        "payload": {"content": doc["content"], "source": doc["source"], "chunk_index": 0}
    })

# Upsert points to Qdrant
qdrant_client.upsert(
    collection_name=collection_name,
    points=points
)

print(f"Added {len(points)} test points to '{collection_name}'")


retriever = RAGRetriever()
result = retriever.retrieve("What is ROS 2?")
print(result)