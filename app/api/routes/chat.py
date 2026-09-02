from fastapi import APIRouter
from pydantic import BaseModel

from app.rag_pipeline import RAGPipeline


class AskRequest(BaseModel):
    question: str


def create_chat_router(
    pipeline: RAGPipeline,
) -> APIRouter:

    router = APIRouter(
        prefix="/chat",
        tags=["Chat"],
    )

    @router.post("/ask")
    def ask(request: AskRequest):
        answer = pipeline.ask(
            request.question
        )

        return {
            "question": request.question,
            "answer": answer,
        }

    return router