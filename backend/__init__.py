logger.info(f"QdrantClient type: {type(self.qdrant_client)}")
logger.info(f"QdrantClient dir contains search: {'search' in dir(self.qdrant_client)}")
