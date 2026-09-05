from pathlib import Path

from qdrant_client import QdrantClient

from app.ingestion.pipeline import ingest_document
from app.retrieval.embeddings import EmbeddingService
from app.retrieval.vector_store import VectorStore
from app.evaluation.evaluator import CandidateEvaluator


class DocumentService:

    def __init__(self, client: QdrantClient | None = None):
        self.embedding_service = EmbeddingService()

        self.vector_store = VectorStore(
            client=client
        )

        self.evaluator = CandidateEvaluator()

    def index_document(
        self,
        file_path: str,
    ) -> dict:

        path = Path(file_path)

        if not path.exists():
            raise FileNotFoundError(
                f"Document not found: {file_path}"
            )

        # 1. Ingest document
        chunks = ingest_document(file_path)

        # 2. Extract chunk text
        texts = [
            chunk.content
            for chunk in chunks
        ]

        # 3. Evaluate candidate
        candidate_text = "\n".join(texts)

        evaluation = self.evaluator.evaluate(
            candidate_text
        )

        # 4. Generate embeddings
        embeddings = self.embedding_service.embed_documents(
            texts
        )

        # 5. Create Qdrant payloads
        payloads = []

        for chunk in chunks:
            payloads.append(
                {
                    "text": chunk.content,
                    "source": path.name,
                    "chunk_id": chunk.chunk_id,
                    "start_index": chunk.start_index,
                    "end_index": chunk.end_index,
                }
            )

        # 6. Store vectors
        self.vector_store.add_documents(
            embeddings=embeddings,
            payloads=payloads,
        )

        return {
            "filename": path.name,
            "chunks": len(chunks),
            "vectors": len(embeddings),
            "status": "indexed",
            "evaluation": evaluation,
        }
