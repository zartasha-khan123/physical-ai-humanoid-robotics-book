# Actionable Tasks for Spec-3: RAG Agent + FastAPI Backend

**Feature**: `rag-agent-backend`

This document outlines the actionable tasks for implementing the RAG Agent and FastAPI Backend integration as defined in Spec-3.

## Phase 1: Setup

- [ ] T001 Initialize a new Python project directory named `rag_backend`.
- [ ] T002 Create a `requirements.txt` file and add initial dependencies: `fastapi`, `uvicorn`, `qdrant-client`, `openai`, `pydantic`, `python-dotenv`.
- [ ] T003 Create `rag_backend/config.py` to manage environment variables and settings (e.g., Qdrant host, OpenAI API key).
- [ ] T004 Create a `.env.example` file with placeholders for environment variables.
- [ ] T005 Set up a virtual environment and install dependencies.

## Phase 2: Core Components

- [ ] T006 Create `rag_backend/qdrant_utils.py` to encapsulate Qdrant client interactions.
- [ ] T007 Implement `initialize_qdrant_client()` function in `qdrant_utils.py` to connect to Qdrant.
- [ ] T008 Implement `retrieve_chunks(query: str, top_k: int, selected_ids: list[str] = None)` function in `qdrant_utils.py` as per the plan.
- [ ] T009 Create `rag_backend/agent.py` to house the `RAGAgent` class.
- [ ] T010 Implement the `RAGAgent` class in `agent.py` with an `__init__` method to load necessary configurations.
- [ ] T011 Implement `generate_answer(query: str, selected_ids: list[str] = None)` method in `RAGAgent` to orchestrate retrieval and generation.

## Phase 3: FastAPI Backend

- [ ] T012 Create `rag_backend/main.py` for the FastAPI application.
- [ ] T013 Define Pydantic models for request (`QueryRequest`) and response (`QueryResponse`) in `main.py`.
- [ ] T014 Implement the `POST /query` endpoint in `main.py` to accept user queries.
- [ ] T015 Integrate the `RAGAgent` into the `POST /query` endpoint to process requests.
- [ ] T016 Ensure the `/query` endpoint returns the generated `answer` and `metadata` in the `QueryResponse` format.

## Phase 4: Enhancements

- [ ] T017 Configure Python's `logging` module in `main.py` and `agent.py`.
- [ ] T018 Add log statements for incoming queries, retrieved chunks, and generated answers.
- [ ] T019 Implement custom exception handlers for common errors (e.g., Qdrant connection issues, OpenAI API errors).
- [ ] T020 Ensure proper error logging for all exceptions.

## Phase 5: Testing & Documentation

- [ ] T021 Create a `tests/test_backend.py` file for minimal test scripts.
- [ ] T022 Write a test case for full-book retrieval (`/query` with `selected_ids=None`) using `pytest` or similar.
- [ ] T023 Write a test case for partial selection retrieval (`/query` with `selected_ids`) using `pytest` or similar.
- [ ] T024 Validate that test responses include accurate metadata (source URL, chunk ID, section/page).
- [ ] T025 Document the `/query` endpoint in `rag_backend/main.py` using FastAPI's docstrings, including input/output formats.
- [ ] T026 Document the module structure and usage in a `README.md` file at the root of `rag_backend`.
- [ ] T027 Include sample test queries and their expected outputs in the `README.md` or a dedicated `examples.md` file.

## Dependencies

- **T006-T008 (Qdrant Utils)** are prerequisites for **T010-T011 (RAG Agent)**.
- **T010-T011 (RAG Agent)** are prerequisites for **T014-T016 (FastAPI Endpoint)**.
- **Phase 1 (Setup)** is a prerequisite for all subsequent phases.

## Implementation Strategy

- Implement tasks sequentially within each phase, respecting stated dependencies.
- Leverage FastAPI's built-in validation and dependency injection for cleaner code.
- Prioritize core functionality before adding extensive error handling or advanced logging.
