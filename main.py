from fastapi import FastAPI
from pydantic import BaseModel
from qdrant_client import QdrantClient

from app.config import settings
from app.rag_pipeline import RAGPipeline
from app.api.routes.documents import create_document_router

app = FastAPI(
    title="RecruitRAG-AI",
    description="AI-powered recruitment RAG system",
    version="1.0.0",
)

# ==========================================================
# Shared Qdrant Client
# ==========================================================

if settings.qdrant_url and settings.qdrant_api_key:
    qdrant_client = QdrantClient(
        url=settings.qdrant_url,
        api_key=settings.qdrant_api_key,
    )
else:
    qdrant_client = QdrantClient(
        path="qdrant_data",
        force_disable_check_same_thread=True,
    )

# ==========================================================
# RAG Pipeline
# ==========================================================

pipeline = RAGPipeline(
    client=qdrant_client
)

# ==========================================================
# Document Routes
# ==========================================================

documents_router = create_document_router(
    client=qdrant_client
)

app.include_router(documents_router)

# ==========================================================
# Request Model
# ==========================================================

class AskRequest(BaseModel):
    question: str

# ==========================================================
# Root
# ==========================================================

@app.get("/")
def root():
    return {
        "message": "RecruitRAG-AI API is running",
        "status": "healthy",
    }

# ==========================================================
# Health
# ==========================================================

@app.get("/health")
def health():
    return {
        "status": "ok",
    }

# ==========================================================
# Ask
# ==========================================================

@app.post("/ask")
def ask(request: AskRequest):
    answer = pipeline.ask(
        request.question
    )

    return {
        "question": request.question,
        "answer": answer,
    }