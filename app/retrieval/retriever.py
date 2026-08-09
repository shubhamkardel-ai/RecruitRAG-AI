from dataclasses import dataclass
from typing import List

from qdrant_client import QdrantClient

from app.retrieval.embeddings import EmbeddingService
from app.retrieval.vector_store import VectorStore


@dataclass
class RetrievedDocument:
    text: str
    source: str
    chunk_id: int
    score: float


class Retriever:
    """
    Retrieves the most relevant document chunks from Qdrant.
    """

    def __init__(self, client: QdrantClient | None = None):
        self.embedding_service = EmbeddingService()

        self.vector_store = VectorStore(
            client=client
        )

    def retrieve(
        self,
        query: str,
        top_k: int = 5,
    ) -> List[RetrievedDocument]:

        query_vector = self.embedding_service.embed_text(query)

        results = self.vector_store.search(
            query_vector=query_vector,
            limit=top_k,
        )

        documents = []

        for result in results:
            payload = result.payload or {}

            documents.append(
                RetrievedDocument(
                    text=payload.get("text", ""),
                    source=payload.get("source", "unknown"),
                    chunk_id=payload.get("chunk_id", -1),
                    score=float(result.score),
                )
            )

        return documents