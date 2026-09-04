from fastembed import TextEmbedding


class EmbeddingService:
    """
    Generates vector embeddings for documents and queries
    using Qdrant FastEmbed.
    """

    def __init__(
        self,
        model_name: str = "BAAI/bge-small-en-v1.5",
    ):
        self.model_name = model_name
        self.model = TextEmbedding(model_name=model_name)
        self.dimension = 384

    def embed_text(self, text: str) -> list[float]:
        """
        Generate an embedding for a single text.
        """

        if not text or not text.strip():
            raise ValueError("Text cannot be empty.")

        embedding = next(self.model.embed([text]))

        return embedding.tolist()

    def embed_documents(
        self,
        texts: list[str],
    ) -> list[list[float]]:
        """
        Generate embeddings for multiple document chunks.
        """

        if not texts:
            return []

        embeddings = self.model.embed(texts)

        return [embedding.tolist() for embedding in embeddings]

    def embedding_dimension(self) -> int:
        """
        Return the dimensionality of the embedding model.
        """

        return self.dimension