from app.ingestion.pipeline import ingest_document
from app.retrieval.embeddings import EmbeddingService
from app.retrieval.vector_store import VectorStore


def main():
    print("Starting retrieval test...\n")

    # --------------------------------------------------
    # 1. Ingest document
    # --------------------------------------------------

    chunks = ingest_document(
        "data/raw/sample_resume.txt"
    )

    print(f"Chunks created: {len(chunks)}")

    # --------------------------------------------------
    # 2. Create embedding service
    # --------------------------------------------------

    embedding_service = EmbeddingService()

    print(
        "Embedding dimension:",
        embedding_service.embedding_dimension(),
    )

    # --------------------------------------------------
    # 3. Generate embeddings
    # --------------------------------------------------

    texts = [
        chunk.content
        for chunk in chunks
    ]

    embeddings = embedding_service.embed_documents(
        texts
    )

    print(
        f"Embeddings generated: {len(embeddings)}"
    )

    # --------------------------------------------------
    # 4. Create Qdrant vector store
    # --------------------------------------------------

    vector_store = VectorStore(
        vector_size=embedding_service.embedding_dimension()
    )

    # --------------------------------------------------
    # 5. Store chunks
    # --------------------------------------------------

    payloads = [
        {
            "text": chunk.content,
            "chunk_id": chunk.chunk_id,
            "source": "sample_resume.txt",
        }
        for chunk in chunks
    ]

    vector_store.add_documents(
        embeddings=embeddings,
        payloads=payloads,
    )

    print(
        "Vectors stored:",
        vector_store.count(),
    )

    # --------------------------------------------------
    # 6. Test semantic search
    # --------------------------------------------------

    query = "What machine learning projects has the candidate built?"

    print(f"\nQuery: {query}")

    query_vector = embedding_service.embed_text(
        query
    )

    results = vector_store.search(
        query_vector=query_vector,
        limit=3,
    )

    print("\nSearch results:")

    for result in results:
        print("\nScore:", result.score)
        print("Payload:", result.payload)

    print("\nRetrieval test completed successfully.")


if __name__ == "__main__":
    main()