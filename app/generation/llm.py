import os

from dotenv import load_dotenv
from groq import Groq


load_dotenv()


class LLMService:
    """
    Service responsible for communicating with the Groq LLM.
    """

    def __init__(self):
        self.api_key = os.getenv("GROQ_API_KEY")
        self.model = os.getenv(
            "LLM_MODEL",
            "openai/gpt-oss-120b"
        )

        if not self.api_key:
            raise ValueError(
                "GROQ_API_KEY is not configured. "
                "Add it to your .env file."
            )

        self.client = Groq(
            api_key=self.api_key
        )

    def generate(
            self,
            prompt: str,
            temperature: float = 0.2,
            max_tokens: int = 2048,
    ) -> str:
        """
        Generate a response using the configured Groq model.
        """

        response = self.client.chat.completions.create(
            model=self.model,
            messages=[
                {
                    "role": "system",
                    "content": (
                        "You are RecruitRAG-AI, "
                        "an intelligent recruitment assistant. "
                        "Answer using the provided context. "
                        "Do not invent candidate information."
                    ),
                },
                {
                    "role": "user",
                    "content": prompt,
                },
            ],
            temperature=temperature,
            max_completion_tokens=max_tokens,
        )

        return response.choices[0].message.content.strip()
