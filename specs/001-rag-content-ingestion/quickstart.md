# Quickstart: RAG Content Ingestion Pipeline

## Prerequisites

- Python 3.11+
- Access to OpenAI API (or compatible embedding service)
- Qdrant Cloud account with API key
- Target Docusaurus website URLs ready

## Setup

### 1. Clone and Install Dependencies
```bash
git clone [repository-url]
cd [repository-name]
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
```

### 2. Configure Environment Variables
Create a `.env` file in the project root:
```env
OPENAI_API_KEY=your_openai_api_key
QDRANT_API_KEY=your_qdrant_api_key
QDRANT_HOST=your_qdrant_cluster_url
QDRANT_COLLECTION_NAME=rag_content_chunks
EMBEDDING_MODEL=text-embedding-ada-002
CHUNK_SIZE=512
CHUNK_OVERLAP=50
```

### 3. Install Required Packages
```bash
pip install requests beautifulsoup4 openai qdrant-client tiktoken python-dotenv
```

## Basic Usage

### Ingest Content from a Website
```bash
python -m cli.main ingest --url https://your-docusaurus-site.com --collection rag_content_chunks
```

### Ingest from Multiple URLs
```bash
python -m cli.main ingest --url https://site1.com --url https://site2.com
```

### Ingest from a File of URLs
```bash
python -m cli.main ingest --urls-file urls.txt
```

Where `urls.txt` contains one URL per line.

## Configuration Options

### Chunking Parameters
- `--chunk-size`: Size of text chunks in tokens (default: 512)
- `--chunk-overlap`: Overlap between chunks in tokens (default: 50)
- `--min-chunk-size`: Minimum size for a chunk (default: 100)

### Processing Parameters
- `--batch-size`: Number of chunks to process per API call (default: 10)
- `--max-concurrent`: Maximum concurrent requests (default: 5)
- `--retries`: Number of retry attempts for failed requests (default: 3)

## Verification

### Test Similarity Search
```bash
python -m cli.main search --query "your search query" --limit 5
```

### Check Stored Content
```bash
python -m cli.main status
```

## Common Commands

### Full Ingestion Pipeline
```bash
# Extract, process, embed, and store content
python -m cli.main full-pipeline --url https://your-site.com

# With custom parameters
python -m cli.main full-pipeline --url https://your-site.com --chunk-size 768 --batch-size 15
```

### Incremental Update
```bash
# Update only changed content
python -m cli.main incremental --url https://your-site.com
```

### Clean Up
```bash
# Remove all content from a collection
python -m cli.main cleanup --collection rag_content_chunks --confirm
```

## Troubleshooting

### Common Issues
- **Rate Limiting**: Reduce `--batch-size` and `--max-concurrent` values
- **Memory Issues**: Process smaller batches or use `--chunk-size` with lower values
- **Authentication**: Verify API keys in `.env` file

### Enable Verbose Logging
```bash
python -m cli.main ingest --url https://your-site.com --verbose
```

## Next Steps

1. **Customize chunking strategy** based on your content type
2. **Tune embedding parameters** for your specific use case
3. **Set up monitoring** for production usage
4. **Implement incremental updates** for regularly changing content