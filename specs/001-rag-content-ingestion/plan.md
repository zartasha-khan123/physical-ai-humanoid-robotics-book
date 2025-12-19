# Implementation Plan: RAG Content Ingestion Pipeline

**Branch**: `001-rag-content-ingestion` | **Date**: 2025-12-16 | **Spec**: [specs/001-rag-content-ingestion/spec.md](specs/001-rag-content-ingestion/spec.md)
**Input**: Feature specification from `/specs/001-rag-content-ingestion/spec.md`

**Note**: This template is filled in by the `/sp.plan` command. See `.specify/templates/commands/plan.md` for the execution workflow.

## Summary

Implementation of a content ingestion pipeline that extracts text from Docusaurus-based websites, processes and chunks the content, generates vector embeddings using an OpenAI-compatible model, and stores the embeddings in Qdrant Cloud with proper metadata. The pipeline supports idempotent re-ingestion to prevent duplicates and enables efficient similarity searches for RAG applications.

## Technical Context

**Language/Version**: Python 3.11
**Primary Dependencies**: requests, beautifulsoup4, openai, qdrant-client, tiktoken, lxml
**Storage**: Qdrant Cloud (vector database), local file system for configuration
**Testing**: pytest with integration tests for API calls and vector operations
**Target Platform**: Linux server (can run on Windows/Mac for development)
**Project Type**: single (CLI-based processing pipeline)
**Performance Goals**: Process 100+ pages within 10 minutes, embedding generation under 1 second per chunk
**Constraints**: Must work within Qdrant Cloud Free Tier limits, support re-ingestion without duplicates
**Scale/Scope**: Handle 1000+ pages, 10k+ content chunks, support incremental updates

## Constitution Check

*GATE: Must pass before Phase 0 research. Re-check after Phase 1 design.*

The implementation follows the project constitution principles:
- **Test-First**: All components will have unit and integration tests
- **CLI Interface**: Pipeline will be accessible via command-line interface
- **Observability**: Structured logging for tracking pipeline progress and errors
- **Library-First**: Core functionality will be organized as reusable libraries

## System Design and Workflow for main.py

### Functions to Implement

1. **get_all_urls()**
   - **Purpose**: Fetch all deployed URLs from "https://physical-ai-book-jade.vercel.app"
   - **Implementation**: Use requests to fetch the sitemap or crawl the website to discover all pages
   - **Output**: List of valid URLs to process

2. **extract_text_from_url(url)**
   - **Purpose**: Extract clean text from HTML content
   - **Implementation**: Use BeautifulSoup4 with lxml parser to extract text from main content areas while removing navigation, headers, footers
   - **Output**: Clean text content as a string

3. **chunk_text(text, min_tokens=200, max_tokens=1000, overlap=10-20%)**
   - **Purpose**: Split text into overlapping chunks
   - **Implementation**: Recursive character splitting with priority on natural breaks (sentences, paragraphs)
   - **Output**: List of text chunks with appropriate size and overlap

4. **embed(text_chunks)**
   - **Purpose**: Generate embeddings for each chunk using the chosen embedding model and batching strategy
   - **Implementation**: Use OpenAI API with batching to efficiently process multiple chunks
   - **Output**: List of embedding vectors corresponding to each text chunk

5. **create_collection(name="rag_embedding")**
   - **Purpose**: Create a Qdrant collection named "rag_embedding" if it does not exist
   - **Implementation**: Use qdrant-client to check for collection existence and create if needed with appropriate vector size
   - **Output**: Confirmation that collection exists

6. **save_chunk_to_qdrant(chunk, embedding)**
   - **Purpose**: Save each chunk and its embedding to Qdrant
   - **Implementation**: Store chunk text with embedding vector and metadata (source URL, chunk index, etc.)
   - **Output**: Confirmation of successful storage with unique ID

### Execution Flow (main())

The main execution flow will implement the following sequence:

1. **Initialize**: Set up configuration and Qdrant connection
2. **Create Collection**: Ensure "rag_embedding" collection exists
3. **Get URLs**: Call `get_all_urls()` to retrieve deployed URLs from "https://physical-ai-book-jade.vercel.app"
4. **Process Each URL**: For each URL in the list:
   a. **Extract Text**: Call `extract_text_from_url(url)` to get clean content
   b. **Chunk Text**: Call `chunk_text()` with specified parameters to split content
   c. **Generate Embeddings**: Call `embed()` to create vector representations
   d. **Store in Qdrant**: For each chunk/embedding pair, call `save_chunk_to_qdrant()`
5. **Complete**: Log summary of processed content and exit

### Error Handling and Validation

- Implement retry logic for network requests
- Validate chunk sizes meet minimum requirements
- Confirm successful storage in Qdrant before proceeding
- Log progress and errors for monitoring

## Project Structure

### Documentation (this feature)

```text
specs/001-rag-content-ingestion/
├── plan.md              # This file (/sp.plan command output)
├── research.md          # Phase 0 output (/sp.plan command)
├── data-model.md        # Phase 1 output (/sp.plan command)
├── quickstart.md        # Phase 1 output (/sp.plan command)
├── contracts/           # Phase 1 output (/sp.plan command)
└── tasks.md             # Phase 2 output (/sp.tasks command - NOT created by /sp.plan)
```

### Source Code (repository root)

```text
src/
├── rag_ingestion/
│   ├── __init__.py
│   ├── extractor.py          # HTML content extraction from Docusaurus sites
│   ├── processor.py          # Text cleaning and preprocessing
│   ├── chunker.py            # Content chunking with size and boundary rules
│   ├── embedder.py           # Vector embedding generation
│   ├── storage.py            # Qdrant Cloud integration
│   ├── pipeline.py           # Main orchestration logic
│   └── utils.py              # Helper functions
├── cli/
│   └── main.py               # Command-line interface
└── config/
    └── settings.py           # Configuration management

tests/
├── unit/
│   ├── test_extractor.py
│   ├── test_chunker.py
│   ├── test_embedder.py
│   └── test_storage.py
├── integration/
│   └── test_pipeline.py
└── fixtures/
    └── sample_content.html
```

**Structure Decision**: Single project structure chosen as this is a CLI-based processing pipeline. The core functionality is organized as reusable libraries under rag_ingestion/, with a CLI interface for execution and comprehensive test coverage.

## Complexity Tracking

> **Fill ONLY if Constitution Check has violations that must be justified**

| Violation | Why Needed | Simpler Alternative Rejected Because |
|-----------|------------|-------------------------------------|
| [N/A] | [N/A] | [N/A] |
