

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import logging
from backend.retriving import RAGRetriever

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"]
)

retriever = RAGRetriever()


class QueryRequest(BaseModel):
    query: str


@app.post("/query")
async def query(payload: QueryRequest):
    user_query = payload.query.strip()

    if not user_query:
        return {"error": "Empty query", "status": "error"}

    logger.info(f"Query received: {user_query}")

    try:
        return await retriever.retrieve(user_query)
    except Exception as e:
        logger.error(f"Error during retrieval: {e}")
        return {"answer": "Sorry, something went wrong.", "metadata": []}
