from typing import Any

from qdrant_client import QdrantClient
from qdrant_client.models import Distance, PointStruct, VectorParams


class VectorStore:
    """
    Qdrant vector store for RecruitRAG-AI.

    Handles:
    - Collection creation
    - Vector insertion
    - Vector search
    """

    def __init__(
        self,
        collection_name: str = "recruitrag_documents",
        vector_size: int = 384,
        path: str = "qdrant_data",
    ):
        self.collection_name = collection_name
        self.vector_size = vector_size

        # Local Qdrant storage.
        # This keeps development simple without requiring
        # a separate Qdrant server.
        self.client = QdrantClient(path=path)

        self._create_collection()

    def _create_collection(self) -> None:
        """Create the collection if it does not already exist."""

        collections = self.client.get_collections().collections

        existing_names = {
            collection.name
            for collection in collections
        }

        if self.collection_name not in existing_names:
            self.client.create_collection(
                collection_name=self.collection_name,
                vectors_config=VectorParams(
                    size=self.vector_size,
                    distance=Distance.COSINE,
                ),
            )

    def add_documents(
        self,
        embeddings: list[list[float]],
        payloads: list[dict[str, Any]],
    ) -> None:
        """
        Store document embeddings and metadata in Qdrant.
        """

        if len(embeddings) != len(payloads):
            raise ValueError(
                "Embeddings and payloads must have the same length."
            )

        if not embeddings:
            return

        points = []

        for index, (embedding, payload) in enumerate(
            zip(embeddings, payloads)
        ):
            points.append(
                PointStruct(
                    id=index,
                    vector=embedding,
                    payload=payload,
                )
            )

        self.client.upsert(
            collection_name=self.collection_name,
            points=points,
        )

    def search(
        self,
        query_vector: list[float],
        limit: int = 5,
    ):
        """
        Search Qdrant for the most semantically similar chunks.
        """

        if not query_vector:
            raise ValueError("Query vector cannot be empty.")

        return self.client.query_points(
            collection_name=self.collection_name,
            query=query_vector,
            limit=limit,
        ).points

    def count(self) -> int:
        """Return the number of stored vectors."""

        result = self.client.count(
            collection_name=self.collection_name,
            exact=True,
        )

        return result.count