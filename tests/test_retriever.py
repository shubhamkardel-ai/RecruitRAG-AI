from app.retrieval.embeddings import EmbeddingService
from app.retrieval.vector_store import VectorStore
from app.retrieval.retriever import Retriever


def main():
    print("Starting retriever test...\n")

    # 1. Create embedding service
    embedding_service = EmbeddingService()

    print(
        "Embedding dimension:",
        embedding_service.embedding_dimension(),
    )

    # 2. Connect to local Qdrant
    vector_store = VectorStore(
        vector_size=embedding_service.embedding_dimension()
    )

    print(
        "Vectors available:",
        vector_store.count(),
    )

    # 3. Create retriever
    retriever = Retriever(
        embedding_service=embedding_service,
        vector_store=vector_store,
        top_k=3,
    )

    # 4. User question
    query = (
        "What AI and machine learning projects "
        "has the candidate built?"
    )

    print(f"\nQuery: {query}")

    # 5. Retrieve relevant chunks
    documents = retriever.retrieve(query)

    print(
        f"\nDocuments retrieved: {len(documents)}"
    )

    # 6. Display results
    for index, document in enumerate(
        documents,
        start=1,
    ):
        print(f"\n--- Result {index} ---")
        print(f"Score: {document.score:.4f}")
        print(f"Source: {document.source}")
        print(f"Chunk ID: {document.chunk_id}")
        print(f"Content:\n{document.content}")

    print("\nRetriever test completed successfully.")


if __name__ == "__main__":
    main()