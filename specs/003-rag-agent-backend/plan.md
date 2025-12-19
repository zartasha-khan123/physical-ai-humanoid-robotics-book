# Technical Execution Plan: RAG Agent + FastAPI Backend (Spec-3)

**Feature Branch**: `feature/rag-agent-backend`
**Created**: 2025-12-08
**Status**: Draft

## 1. Scope and Dependencies

### In Scope
-   **RAG Agent Module**: A Python module encapsulating the logic for retrieval-augmented generation.
-   **FastAPI Server**: A server that exposes the RAG agent's functionality via a REST API.
-   **Qdrant Integration**: Connecting to and retrieving data from the Qdrant vector database created in Spec-2.
-   **OpenAI Agent Integration**: Using the OpenAI Agents SDK to generate answers based on retrieved context.
-   **API Endpoints**: Implementation of a `/query` endpoint.
-   **Error Handling & Logging**: Basic mechanisms for logging events and handling exceptions.
-   **Testing**: Minimal scripts to validate the backend's functionality.

### Out of Scope
-   Frontend UI development.
-   User authentication and authorization.
-   Advanced multi-agent orchestration.
-   Deployment infrastructure setup (beyond providing a containerizable application).

### Dependencies
-   **Spec-2 Retrieval Pipeline**: A functional Qdrant database populated with embeddings from the Docusaurus book content.
-   **Python 3.10+**: The programming language for the backend.
-   **OpenAI API Key**: Required for the generation step.

## 2. Key Libraries and SDKs

-   **Backend Framework**: `FastAPI`
-   **Vector Database Client**: `qdrant-client`
-   **LLM SDK**: `openai` (specifically the Agents SDK)
-   **Data Validation**: `pydantic` (used by FastAPI)
-   **Environment Management**: `python-dotenv`

## 3. Execution Plan (Step-by-Step)

### Step 1: Project Scaffolding
-   **Task**: Set up the project structure.
-   **Details**:
    -   Create a main directory `rag_backend`.
    -   Inside `rag_backend`, create `main.py` for the FastAPI app, `agent.py` for the RAG logic, `qdrant_utils.py` for Qdrant interaction, and `config.py` for settings.
    -   Initialize a `requirements.txt` file with the necessary libraries.
-   **Output**: A structured project directory with empty Python files.

### Step 2: Qdrant Integration
-   **Task**: Implement the retrieval logic from the Spec-2 pipeline.
-   **Details**:
    -   In `config.py`, define variables for Qdrant host and API key.
    -   In `qdrant_utils.py`, create a function `retrieve_chunks(query: str, top_k: int, selected_ids: list[str] = None)` that:
        -   Connects to the Qdrant client.
        -   If `selected_ids` are provided, fetches those specific chunks.
        -   If not, converts the `query` to an embedding (using the same model as Spec-2) and performs a similarity search.
        -   Returns the top-k relevant chunks with their metadata.
-   **Input**: A user query (string) and optional chunk IDs.
-   **Output**: A list of documents/chunks from Qdrant.

### Step 3: RAG Agent Orchestration
-   **Task**: Define the core agent logic that combines retrieval and generation.
-   **Details**:
    -   In `agent.py`, create a class `RAGAgent`.
    -   The `RAGAgent` will have a method `generate_answer(query: str, selected_ids: list[str] = None)`.
    -   This method will:
        1.  Call `qdrant_utils.retrieve_chunks` to get the context.
        2.  Format the retrieved chunks into a string prompt for the OpenAI Agent.
        3.  Instantiate and run the OpenAI Agent with the prompt.
        4.  The agent's instructions will be to answer the query based *only* on the provided context.
        5.  Extract the generated answer and the metadata of the source chunks.
-   **Input**: A user query and optional chunk IDs.
-   **Output**: A dictionary containing the `answer` and a list of `sources` with metadata.

### Step 4: FastAPI Endpoint Implementation
-   **Task**: Expose the RAG agent through a FastAPI endpoint.
-   **Details**:
    -   In `main.py`, create a FastAPI app instance.
    -   Define Pydantic models for the request (`QueryRequest`) and response (`QueryResponse`).
    -   Implement the `POST /query` endpoint:
        -   It will accept a `QueryRequest` body with a `query` (string) and an optional `selected_text` (list of strings/IDs).
        -   Instantiate `RAGAgent`.
        -   Call the `generate_answer` method with the request data.
        -   Return the result as a `QueryResponse`.
    -   Implement basic error handling using FastAPI's exception handling mechanisms.
-   **Input**: A JSON object with `query` and optional `selected_text`.
-   **Output**: A JSON object with `answer` and `sources`.

### Step 5: Logging and Configuration
-   **Task**: Add logging and centralize configuration.
-   **Details**:
    -   Use Python's built-in `logging` module.
    -   Configure a basic logger in `main.py` to log events to the console.
    -   Add log statements in the agent and API endpoint for key events (e.g., received query, chunks retrieved, answer generated).
    -   Ensure all secrets (like OpenAI API key) and configurations are loaded from environment variables using `python-dotenv`.

## 4. Data Flow

```
1. User Query (JSON)
       |
       v
2. FastAPI Endpoint (`POST /query`)
       |
       v
3. RAG Agent (`generate_answer`)
       |
       v
4. Qdrant Utils (`retrieve_chunks`) ----> [Qdrant DB]
       |                                      ^
       |<------ 5. Relevant Chunks -----------|
       |
       v
6. OpenAI Agent (constructs prompt) ----> [OpenAI API]
       |                                      ^
       |<------ 7. Generated Answer ----------|
       |
       v
8. FastAPI Endpoint (formats response)
       |
       v
9. User Response (JSON)
```

## 5. Test Strategy

-   **Unit Tests**:
    -   Mock the Qdrant client and OpenAI API.
    -   Write a test for the `RAGAgent` to ensure it correctly formats prompts and processes responses.
-   **Integration Tests**:
    -   Create a small, temporary Qdrant collection with a few sample documents.
    -   Write a test script (`test_backend.py`) that uses the `requests` library to:
        1.  Send a full-book query to the running FastAPI server.
        2.  Send a selected-text query.
        3.  Validate that the responses are in the correct format and contain the expected keys (`answer`, `sources`).
        4.  Check that the metadata in the response is accurate.
-   **Validation**: The tests will pass if the API returns a `200 OK` status and the response body matches the expected schema.
