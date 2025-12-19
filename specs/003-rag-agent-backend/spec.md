# Feature Specification: RAG Agent and FastAPI Backend Integration

**Feature Branch**: `feature/rag-agent-backend`
**Created**: 2025-12-08
**Status**: Draft

## 1. Overview

This document specifies the design and requirements for a RAG (Retrieval-Augmented Generation) agent and its integration with a FastAPI backend. This system is the third phase of the RAG chatbot project, intended to serve as the core logic for a Docusaurus-based book's AI assistant. The backend will accept user queries, retrieve relevant content from a Qdrant vector database (as defined in Spec-2), use an OpenAI Agent to generate a context-aware answer, and expose this functionality through a set of well-defined FastAPI endpoints.

## 2. User Stories

### User Story 1: Full-Book Query (P1)
**As a backend developer,** I want to create a FastAPI endpoint that accepts a user's question and queries the entire book's content to provide a relevant answer.
- **Why**: To provide a general-purpose query interface for users who have questions about the book's content without a specific context.
- **Acceptance Criteria**:
    1. An endpoint `/query/book` accepts a POST request with a JSON body containing the user's `query`.
    2. The system retrieves relevant chunks from the Qdrant database.
    3. The OpenAI Agent generates an answer based on the retrieved chunks.
    4. The response contains the generated answer and metadata (source URL, chunk ID) for each cited source.

### User Story 2: Selected-Text Query (P1)
**As a backend developer,** I want to create a FastAPI endpoint that accepts a user's question and a list of selected text/chunk IDs to provide a contextually-limited answer.
- **Why**: To allow for more focused queries when the user has already highlighted relevant sections of the book.
- **Acceptance Criteria**:
    1. An endpoint `/query/selection` accepts a POST request with a JSON body containing the `query` and a list of `chunk_ids`.
    2. The system retrieves the content for the specified `chunk_ids` from Qdrant.
    3. The OpenAI Agent generates an answer based *only* on the provided chunks.
    4. The response contains the generated answer and the corresponding metadata.

### User Story 3: System Logging (P2)
**As an AI engineer,** I want the system to log all major events, including incoming queries, retrieved chunks, generated answers, and any errors.
- **Why**: To facilitate debugging, monitoring, and performance analysis of the RAG pipeline.
- **Acceptance Criteria**:
    1. All API requests and responses are logged.
    2. Errors and exceptions during retrieval or generation are logged with stack traces.
    3. Logs are structured (e.g., JSON format) for easier parsing.

## 3. Functional Requirements

- **FR-001**: The system MUST provide a RAG agent module responsible for the core retrieval and generation logic.
- **FR-002**: The RAG agent MUST connect to the Qdrant database instance defined in Spec-2.
- **FR-003**: The agent MUST use the OpenAI Agents SDK (or a compatible library like ChatKit) to generate responses.
- **FR-004**: The system MUST provide a FastAPI server to expose the RAG agent's functionality.
- **FR-005**: The FastAPI server MUST implement the API endpoints defined in the "API Endpoint Definitions" section.
- **FR-006**: The system MUST be implemented in Python.
- **FR-007**: The system MUST include minimal test scripts to validate the functionality of the RAG agent and the FastAPI endpoints.

## 4. Non-Functional Requirements

- **NFR-001 (Performance)**: The backend MUST handle at least 5 concurrent queries with a p95 response time under 3 seconds (excluding the OpenAI API latency).
- **NFR-002 (Logging)**: All errors, exceptions, and significant application events MUST be logged to standard output or a configurable log file.
- **NFR-003 (Modularity)**: The RAG agent logic MUST be decoupled from the FastAPI server to allow for independent testing and maintenance.
- **NFR-004 (Deployment)**: The application MUST be containerizable (e.g., with Docker) for easy deployment.

## 5. Key Entities / Modules

- **FastAPI Server (`main.py`)**: The main entry point of the application. Responsible for defining and running the API server and its endpoints.
- **RAG Agent (`rag_agent.py`)**: A module containing the core logic for the RAG pipeline. It will handle query processing, Qdrant retrieval, and interaction with the OpenAI Agent.
- **Qdrant Client (`qdrant_client.py`)**: A helper module to abstract the connection and querying of the Qdrant vector database.
- **Configuration (`config.py`)**: A module to manage application settings, such as Qdrant host, OpenAI API key, etc.

## 6. API Endpoint Definitions

### POST `/query/book`
- **Description**: Submits a query to be answered from the context of the entire book.
- **Request Body**:
  ```json
  {
    "query": "What is the main idea of the book?"
  }
  ```
- **Response Body (Success)**:
  ```json
  {
    "answer": "The main idea of the book is...",
    "metadata": [
      {
        "source_url": "/docs/M1-ROS2/01-Intro-to-ROS2",
        "chunk_id": "chunk_abc123",
        "section": "Introduction"
      }
    ]
  }
  ```
- **Response Body (Error)**:
  ```json
  {
    "detail": "Error processing the query."
  }
  ```

### POST `/query/selection`
- **Description**: Submits a query to be answered from a selected list of text chunks.
- **Request Body**:
  ```json
  {
    "query": "Summarize this section.",
    "chunk_ids": ["chunk_abc123", "chunk_def456"]
  }
  ```
- **Response Body (Success)**:
  ```json
  {
    "answer": "This section discusses...",
    "metadata": [
      {
        "source_url": "/docs/M1-ROS2/01-Intro-to-ROS2",
        "chunk_id": "chunk_abc123",
        "section": "Introduction"
      },
      {
        "source_url": "/docs/M1-ROS2/02-RCLPY-Agents",
        "chunk_id": "chunk_def456",
        "section": "Creating a Publisher"
      }
    ]
  }
  ```

## 7. Success Criteria

- **SC-001**: The FastAPI server runs without errors and exposes the `/query/book` and `/query/selection` endpoints.
- **SC-002**: A test script successfully calls the `/query/book` endpoint and receives a valid, non-empty answer.
- **SC-003**: A test script successfully calls the `/query/selection` endpoint and receives an answer based only on the provided context.
- **SC-004**: All responses include the required metadata (source URL, chunk ID, section/page).
- **SC-005**: Error conditions (e.g., invalid query, Qdrant connection failure) are logged correctly.
- **SC-006**: The codebase is organized into the modules described in the "Key Entities / Modules" section.
