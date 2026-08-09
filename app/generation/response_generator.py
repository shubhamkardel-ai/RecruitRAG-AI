from app.generation.llm import LLMService
from app.generation.prompts import build_prompt


class ResponseGenerator:
    """
    Generates grounded answers from retrieved documents.
    """

    def __init__(self):
        self.llm = LLMService()

    def generate(self, query: str, documents: list) -> str:
        """
        Generate an answer using retrieved documents.
        """

        if not documents:
            return (
                "The information is not available "
                "in the provided documents."
            )

        prompt = build_prompt(
            query=query,
            documents=documents,
        )

        return self.llm.generate(prompt)