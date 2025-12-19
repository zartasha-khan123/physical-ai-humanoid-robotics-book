


# import os
# import time
# import logging
# import asyncio
# import re
# from typing import List, Dict
# from dotenv import load_dotenv

# from openai import OpenAI
# from qdrant_client import QdrantClient

# load_dotenv()

# logging.basicConfig(level=logging.INFO)
# logger = logging.getLogger(__name__)

# def clean_text(text: str) -> str:
#     """Remove code blocks, inline code, markdown headings, diagrams, and HTML tags"""
#     text = re.sub(r"`{3}.*?`{3}", "", text, flags=re.DOTALL)  # code blocks
#     text = re.sub(r"`.*?`", "", text)  # inline code
#     text = re.sub(r"#+\s*", "", text)  # markdown headings
#     text = re.sub(r"\[Diagram:.*?\]", "", text)  # diagram placeholders
#     text = re.sub(r"<.*?>", "", text)  # HTML tags
#     return text.strip()

# class RAGRetriever:
#     def __init__(self):
#         self.collection_name = "rag_embedding"

#         self.openai = OpenAI(
#             api_key=os.getenv("OPENAI_API_KEY")
#         )

#         self.qdrant_client = QdrantClient(
#             url=os.getenv("QDRANT_URL"),
#             api_key=os.getenv("QDRANT_API_KEY"),
#             timeout=60,
#             prefer_grpc=False
#         )

#         logger.info(f"QdrantClient class = {self.qdrant_client.__class__}")

#     # -----------------------------
#     # EMBEDDING (RUN IN THREAD)
#     # -----------------------------
#     async def get_embedding(self, text: str) -> List[float]:
#         response = await asyncio.to_thread(
#             self.openai.embeddings.create,
#             model="text-embedding-ada-002",
#             input=text
#         )
#         return response.data[0].embedding

#     # -----------------------------
#     # QDRANT QUERY (RUN IN THREAD)
#     # -----------------------------
#     async def query_qdrant(
#         self,
#         query_embedding: List[float],
#         top_k: int = 5
#     ) -> List[Dict]:
#         try:
#             response = await asyncio.to_thread(
#                 self.qdrant_client.query_points,
#                 collection_name=self.collection_name,
#                 prefetch=[],
#                 query=query_embedding,
#                 limit=top_k,
#                 with_payload=True
#             )

#             formatted = []
#             for p in response.points:
#                 formatted.append({
#                     "content": p.payload.get("content", ""),
#                     "url": p.payload.get("source", ""),
#                     "position": p.payload.get("chunk_index", 0),
#                     "similarity_score": p.score,
#                 })

#             return formatted

#         except Exception as e:
#             logger.error(f"Qdrant query failed: {e}")
#             return []

#     # -----------------------------
#     # MAIN RETRIEVE (ASYNC)
#     # -----------------------------
#     async def retrieve(self, query_text: str, top_k: int = 5) -> Dict:
#         start = time.time()

#         embedding = await self.get_embedding(query_text)
#         results = await self.query_qdrant(embedding, top_k)

#         if not results:
#             return {
#                 "answer": "I could not find relevant information in the documents.",
#                 "metadata": []
#             }

#         # -------------------------------
#         # CLEAN CONTENT BEFORE GPT
#         # -------------------------------
#         context = "\n\n".join(clean_text(r["content"]) for r in results)

#         prompt = f"""
# Answer the question using ONLY the context below. Write in plain text and ignore any markdown, code, or diagrams.

# Context:
# {context}

# Question:
# {query_text}
# """

#         completion = await asyncio.to_thread(
#             self.openai.chat.completions.create,
#             model="gpt-4o-mini",
#             messages=[
#                 {"role": "system", "content": "You are a documentation assistant."},
#                 {"role": "user", "content": prompt}
#             ]
#         )

#         answer = completion.choices[0].message.content.strip()

#         logger.info(
#             f"Retrieval completed in {(time.time() - start) * 1000:.2f} ms"
#         )

#         return {
#             "answer": answer,
#             "metadata": results
#         }


import os
import time
import logging
import asyncio
import re
from typing import List, Dict
from dotenv import load_dotenv

from openai import OpenAI
from qdrant_client import QdrantClient

load_dotenv()

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def clean_text(text: str) -> str:
    """Remove code blocks, inline code, markdown headings, diagrams, and HTML tags"""
    text = re.sub(r"`{3}.*?`{3}", "", text, flags=re.DOTALL)  # code blocks
    text = re.sub(r"`.*?`", "", text)  # inline code
    text = re.sub(r"#+\s*", "", text)  # markdown headings
    text = re.sub(r"\[Diagram:.*?\]", "", text)  # diagram placeholders
    text = re.sub(r"<.*?>", "", text)  # HTML tags
    return text.strip()

class RAGRetriever:
    def __init__(self):
        self.collection_name = "rag_embedding"

        self.openai = OpenAI(
            api_key=os.getenv("OPENAI_API_KEY")
        )

        self.qdrant_client = QdrantClient(
            url=os.getenv("QDRANT_URL"),
            api_key=os.getenv("QDRANT_API_KEY"),
            timeout=60,
            prefer_grpc=False
        )

        logger.info(f"QdrantClient class = {self.qdrant_client.__class__}")

    # -----------------------------
    # EMBEDDING (RUN IN THREAD)
    # -----------------------------
    async def get_embedding(self, text: str) -> List[float]:
        response = await asyncio.to_thread(
            self.openai.embeddings.create,
            model="text-embedding-ada-002",
            input=text
        )
        return response.data[0].embedding

    # -----------------------------
    # QDRANT QUERY (RUN IN THREAD)
    # -----------------------------
    async def query_qdrant(
        self,
        query_embedding: List[float],
        top_k: int = 5
    ) -> List[Dict]:
        try:
            response = await asyncio.to_thread(
                self.qdrant_client.query_points,
                collection_name=self.collection_name,
                prefetch=[],
                query=query_embedding,
                limit=top_k,
                with_payload=True
            )

            formatted = []
            for p in response.points:
                formatted.append({
                    "content": p.payload.get("content", ""),
                    "url": p.payload.get("source", ""),  # <-- store original source
                    "position": p.payload.get("chunk_index", 0),
                    "similarity_score": p.score,
                })

            return formatted

        except Exception as e:
            logger.error(f"Qdrant query failed: {e}")
            return []

    # -----------------------------
    # MAIN RETRIEVE (ASYNC)
    # -----------------------------
    async def retrieve(self, query_text: str, top_k: int = 5) -> Dict:
        start = time.time()

        embedding = await self.get_embedding(query_text)
        results = await self.query_qdrant(embedding, top_k)

        if not results:
            return {
                "answer": "I could not find relevant information in the documents.",
                "metadata": []
            }

        # -------------------------------
        # CLEAN CONTENT BEFORE GPT
        # -------------------------------
        context = "\n\n".join(clean_text(r["content"]) for r in results)

        # Prepare metadata for frontend
        metadata = []
        for r in results:
            source_url = r.get("url") or "#"
            metadata.append({
                "source_url": source_url,
                "section": os.path.basename(source_url) if source_url != "#" else "Unknown",
                "chunk_index": r.get("position", 0)
            })

        # Prompt for GPT
        prompt = f"""
Answer the question using ONLY the context below. Write in plain text and ignore any markdown, code, or diagrams.

Context:
{context}

Question:
{query_text}
"""

        completion = await asyncio.to_thread(
            self.openai.chat.completions.create,
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": "You are a documentation assistant."},
                {"role": "user", "content": prompt}
            ]
        )

        answer = completion.choices[0].message.content.strip()

        logger.info(f"Retrieval completed in {(time.time() - start) * 1000:.2f} ms")

        return {
            "answer": answer,
            "metadata": metadata  # <-- safe for frontend
        }
