# import os
# import re
# from qdrant_client import QdrantClient, models
# from openai import OpenAI
# from config import QDRANT_URL, QDRANT_API_KEY, OPENAI_API_KEY, COLLECTION_NAME

# # --- Configuration ---
# DOCS_PATH = "../docusaurus-book/docs"
# VECTOR_SIZE = 3072  # Dimension for text-embedding-3-large
# BATCH_SIZE = 16 # Keep batch size small to avoid API rate limits

# # --- Initialize Clients ---
# try:
#     openai_client = OpenAI(api_key=OPENAI_API_KEY)
#     qdrant_client = QdrantClient(url=QDRANT_URL, api_key=QDRANT_API_KEY)
# except Exception as e:
#     print(f"Error initializing clients: {e}")
#     exit()

# def get_markdown_files(root_dir):
#     """Recursively finds all markdown files in a directory."""
#     filepaths = []
#     for dirpath, _, filenames in os.walk(root_dir):
#         for filename in filenames:
#             if filename.endswith(('.md', '.mdx')):
#                 filepaths.append(os.path.join(dirpath, filename))
#     return filepaths

# def parse_markdown(filepath):
#     """Parses a markdown file to extract title and chunks of text."""
#     with open(filepath, 'r', encoding='utf-8') as f:
#         content = f.read()

#     chunks = content.split('\n\n')
#     cleaned_chunks = []
#     for chunk in chunks:
#         chunk = re.sub(r'#+\s.*', '', chunk)
#         chunk = re.sub(r'![.*](.*)', '', chunk)
#         chunk = re.sub(r'\s*`{3}.*?`{3}\s*', '', chunk, flags=re.DOTALL)
#         chunk = chunk.strip()
#         if len(chunk) > 50:
#             cleaned_chunks.append(chunk)

#     title = os.path.basename(filepath).replace('.mdx', '').replace('.md', '')
#     source_url = "/" + os.path.relpath(filepath, DOCS_PATH).replace('\\', '/').replace('.mdx', '').replace('.md', '')
#     return [{"content": chunk, "title": title, "source_url": source_url} for chunk in cleaned_chunks]

# def get_openai_embeddings_batch(texts: list):
#     """Generates embeddings for a batch of texts."""
#     response = openai_client.embeddings.create(
#         model="text-embedding-3-large",
#         input=texts
#     )
#     return [item.embedding for item in response.data]

# def ingest_data():
#     """Main function to ingest data into Qdrant using OpenAI embeddings."""
#     print("Starting data ingestion with OpenAI embeddings...")

#     try:
#         qdrant_client.recreate_collection(
#             collection_name=COLLECTION_NAME,
#             vectors_config=models.VectorParams(size=VECTOR_SIZE, distance=models.Distance.COSINE)
#         )
#         print(f"Collection '{COLLECTION_NAME}' created/recreated with vector size {VECTOR_SIZE}.")
#     except Exception as e:
#         print(f"Could not recreate collection: {e}")
#         return

#     md_files = get_markdown_files(DOCS_PATH)
#     all_chunks_with_metadata = []
#     for filepath in md_files:
#         chunks = parse_markdown(filepath)
#         all_chunks_with_metadata.extend(chunks)
    
#     print(f"Processing {len(all_chunks_with_metadata)} chunks from {len(md_files)} files.")

#     for i in range(0, len(all_chunks_with_metadata), BATCH_SIZE):
#         batch = all_chunks_with_metadata[i:i + BATCH_SIZE]
#         contents = [item['content'] for item in batch]
        
#         print(f"Processing batch {i//BATCH_SIZE + 1}...")
        
#         try:
#             embeddings = get_openai_embeddings_batch(contents)
#             payloads = [{"content": item['content'], "title": item['title'], "source_url": item["source_url"]} for item in batch]
            
#             qdrant_client.upsert(
#                 collection_name=COLLECTION_NAME,
#                 points=models.Batch(ids=None, vectors=embeddings, payloads=payloads)
#             )
#         except Exception as e:
#             print(f"Error processing batch {i//BATCH_SIZE + 1}: {e}")

#     print(f"\nData ingestion complete. Upserted {len(all_chunks_with_metadata)} chunks.")

# if __name__ == "__main__":
#     ingest_data()


import os
import uuid
import logging
from pathlib import Path
from dotenv import load_dotenv

from qdrant_client import QdrantClient
from qdrant_client.http.models import PointStruct, VectorParams, Distance
from openai import OpenAI

# -------------------- SETUP --------------------

load_dotenv()

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

COLLECTION_NAME = "rag_embedding"
DOCS_DIR = Path("../docusaurus-book/docs")
EMBEDDING_MODEL = "text-embedding-ada-002"
VECTOR_SIZE = 1536

openai = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

qdrant = QdrantClient(
    url=os.getenv("QDRANT_URL"),
    api_key=os.getenv("QDRANT_API_KEY"),
)

# -------------------- HELPERS --------------------

def get_embedding(text: str) -> list:
    response = openai.embeddings.create(
        model=EMBEDDING_MODEL,
        input=text
    )
    return response.data[0].embedding


def chunk_text(text: str, chunk_size: int = 500, overlap: int = 100):
    words = text.split()
    chunks = []
    start = 0

    while start < len(words):
        end = start + chunk_size
        chunk = " ".join(words[start:end])
        chunks.append(chunk)
        start = end - overlap

    return chunks


def ensure_collection():
    collections = [c.name for c in qdrant.get_collections().collections]

    if COLLECTION_NAME not in collections:
        logger.info("Creating Qdrant collection...")
        qdrant.create_collection(
            collection_name=COLLECTION_NAME,
            vectors_config=VectorParams(
                size=VECTOR_SIZE,
                distance=Distance.COSINE,
            ),
        )
    else:
        logger.info("Qdrant collection already exists.")


# -------------------- INGESTION --------------------

def ingest_docs():
    ensure_collection()

    points = []
    total_chunks = 0

    for file in DOCS_DIR.rglob("*.md*"):
        try:
            text = file.read_text(encoding="utf-8").strip()
        except Exception as e:
            logger.warning(f"Skipping file {file}: {e}")
            continue

        if not text:
            continue

        chunks = chunk_text(text)

        for idx, chunk in enumerate(chunks):
            embedding = get_embedding(chunk)

            points.append(
                PointStruct(
                    id=str(uuid.uuid4()),
                    vector=embedding,
                    payload={
                        "content": chunk,
                        "source": str(file),
                        "chunk_index": idx,
                    },
                )
            )

            total_chunks += 1

        # Batch upsert every 100 points
        if len(points) >= 25:
            qdrant.upsert(
                collection_name=COLLECTION_NAME,
                points=points,
                wait=True,
            )
            points.clear()

    # Final flush
    if points:
        qdrant.upsert(
            collection_name=COLLECTION_NAME,
            points=points,
            wait=True,
        )

    logger.info(f"Finished ingesting {total_chunks} chunks.")


# -------------------- MAIN --------------------

if __name__ == "__main__":
    ingest_docs()




