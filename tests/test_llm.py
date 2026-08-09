from app.generation.llm import LLMService


def main():
    print("Starting LLM test...\n")

    llm = LLMService()

    prompt = """
You are testing RecruitRAG-AI.

Answer this question in one short sentence:

What is the purpose of a recruitment AI assistant?
"""

    response = llm.generate(prompt)

    print("LLM Response:")
    print(response)

    print("\nLLM test completed successfully.")


if __name__ == "__main__":
    main()