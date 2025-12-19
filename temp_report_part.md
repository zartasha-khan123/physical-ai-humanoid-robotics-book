
### `backend/main.py`
```python
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import Optional, List, Dict

from rag import perform_rag_query

# --- Pydantic Models ---
class QueryRequest(BaseModel):
    query: str
    selected_text: Optional[str] = None

class SourceMetadata(BaseModel):
    source_url: str
    chunk_id: str
    section: str

class QueryResponse(BaseModel):
    answer: str
    metadata: List[SourceMetadata]

# --- FastAPI App ---
app = FastAPI(
    title="RAG Chatbot Backend",
    description="A RAG chatbot backend using FastAPI, OpenAI, and Qdrant.",
    version="1.0.0",
)

# --- CORS Middleware ---
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], # Allows all origins
    allow_credentials=True,
    allow_methods=["*"], # Allows all methods
    allow_headers=["*"], # Allows all headers
)

# --- API Endpoints ---
@app.post("/query", response_model=QueryResponse)
async def query_endpoint(request: QueryRequest):
    """
    Accepts a user query and optional selected text, and returns a RAG-generated answer.
    """
    if not request.query:
        raise HTTPException(status_code=400, detail="Query cannot be empty.")
    
    try:
        result = perform_rag_query(request.query, request.selected_text)
        return result
    except Exception as e:
        print(f"An error occurred during query processing: {e}")
        raise HTTPException(status_code=500, detail="An internal error occurred.")

@app.get("/")
def read_root():
    return {"message": "RAG Chatbot Backend is running."}
```
