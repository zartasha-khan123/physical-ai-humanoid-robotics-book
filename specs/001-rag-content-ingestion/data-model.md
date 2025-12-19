# Data Model: RAG Content Ingestion Pipeline

## Core Entities

### ContentChunk
Represents a semantically coherent segment of extracted text with metadata.

**Fields**:
- `id` (string): Deterministic hash of source_url and chunk_index for idempotency
- `source_url` (string): Original URL where the content was found
- `chunk_index` (integer): Sequential index of this chunk within the source document
- `content` (string): The actual text content of this chunk
- `section_title` (string, optional): Title of the section this chunk belongs to
- `page_title` (string, optional): Title of the source page
- `content_hash` (string): SHA256 hash of the content for change detection
- `vector` (list[float]): The embedding vector representation of the content
- `created_at` (datetime): Timestamp when this chunk was first created
- `updated_at` (datetime): Timestamp when this chunk was last updated

**Validation Rules**:
- `source_url` must be a valid URL
- `content` must not be empty
- `vector` must have the correct dimension for the chosen embedding model
- `chunk_index` must be non-negative

### SourceDocument
Represents a complete document from which chunks are derived.

**Fields**:
- `url` (string): The source URL
- `title` (string): The page title
- `content_hash` (string): Hash of the entire document content
- `last_modified` (datetime): When the document was last updated
- `chunk_count` (integer): Number of chunks extracted from this document
- `metadata` (dict): Additional document-specific metadata

**Validation Rules**:
- `url` must be a valid URL
- `title` must not be empty
- `chunk_count` must be positive

### EmbeddingJob
Represents a complete ingestion job from start to finish.

**Fields**:
- `id` (string): Unique identifier for the job
- `source_urls` (list[string]): List of URLs to process
- `status` (enum): ['pending', 'in_progress', 'completed', 'failed']
- `created_at` (datetime): When the job was started
- `completed_at` (datetime, optional): When the job was completed
- `processed_count` (integer): Number of documents processed
- `error_count` (integer): Number of documents that failed processing
- `metadata` (dict): Additional job-specific metadata

**Validation Rules**:
- `status` must be one of the defined enum values
- `processed_count` and `error_count` must be non-negative

## Relationships

### ContentChunk ↔ SourceDocument
- One SourceDocument can have many ContentChunks (1:N relationship)
- ContentChunk.source_url references SourceDocument.url
- When a SourceDocument is updated, its associated ContentChunks should be reprocessed

### EmbeddingJob ↔ ContentChunk
- One EmbeddingJob can produce many ContentChunks (1:N relationship)
- ContentChunks are associated with an EmbeddingJob via the source URL relationship

## State Transitions

### EmbeddingJob States
```
pending → in_progress → completed
              ↓
            failed
```

- **pending**: Job created but not yet started
- **in_progress**: Job is actively processing documents
- **completed**: All documents processed successfully
- **failed**: One or more documents failed processing

## Indexing Strategy

### Qdrant Collection Schema
```
Collection: rag_content_chunks
Vector size: 1536 (for OpenAI ada-002 embeddings)
Distance: Cosine
```

### Payload Indexes
- Index on `source_url` for efficient retrieval by source
- Index on `content_hash` for change detection
- Index on `created_at` for temporal queries

## Data Flow

### Ingestion Flow
1. **SourceDocument** is created/updated when URL is discovered
2. **ContentChunk** objects are created from SourceDocument content
3. **ContentChunk** objects have embeddings generated and stored
4. **EmbeddingJob** tracks the overall progress of the ingestion

### Update Flow
1. When SourceDocument changes, associated ContentChunks are marked for reprocessing
2. New embeddings are generated for changed chunks
3. Qdrant records are updated with new embeddings while preserving IDs

## Constraints

1. **Uniqueness**: Each combination of source_url and chunk_index must be unique
2. **Integrity**: ContentChunks must reference valid SourceDocuments
3. **Immutability**: Once created, ContentChunk IDs should not change
4. **Idempotency**: Re-running the same job should not create duplicate chunks