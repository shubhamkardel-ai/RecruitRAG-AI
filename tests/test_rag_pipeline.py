from app.rag_pipeline import RAGPipeline


def main():
    print("========================================")
    print("RecruitRAG-AI End-to-End RAG Test")
    print("========================================\n")

    pipeline = RAGPipeline(top_k=3)

    query = "What AI and machine learning projects has the candidate built?"

    print(f"Question: {query}\n")

    answer = pipeline.ask(query)

    print("Answer:")
    print(answer)

    print("\n========================================")
    print("RAG pipeline test completed successfully.")
    print("========================================")


if __name__ == "__main__":
    main()