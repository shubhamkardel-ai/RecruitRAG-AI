from app.retrieval.retriever import Retriever
from app.generation.response_generator import ResponseGenerator


class RAGPipeline:
    """
    End-to-end Retrieval-Augmented Generation pipeline.

    Flow:
        User Query
            ↓
        Retriever
            ↓
        Relevant Documents
            ↓
        Prompt Builder
            ↓
        Groq LLM
            ↓
        Final Answer
    """

    def __init__(self, top_k: int = 5):
        self.retriever = Retriever()
        self.response_generator = ResponseGenerator()
        self.top_k = top_k

    def ask(self, query: str) -> str:
        """
        Answer a user question using retrieved knowledge.
        """

        if not query or not query.strip():
            return "Please provide a question."

        documents = self.retriever.retrieve(
            query=query,
            top_k=self.top_k,
        )

        answer = self.response_generator.generate(
            query=query,
            documents=documents,
        )

        return answer