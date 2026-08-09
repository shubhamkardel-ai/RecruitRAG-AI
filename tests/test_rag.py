from app.rag_pipeline import RAGPipeline


def main():
    print("Starting RecruitRAG-AI...\n")

    pipeline = RAGPipeline(top_k=3)

    query = (
        "What AI and machine learning projects "
        "has the candidate built?"
    )

    print(f"User: {query}\n")

    result = pipeline.answer(query)

    print("RecruitRAG-AI:")
    print(result["answer"])

    print("\nSources:")

    for document in result["documents"]:
        print(
            f"- {document.source} "
            f"(score={document.score:.4f})"
        )

    print("\nRAG pipeline test completed successfully.")


if __name__ == "__main__":
    main()