from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from qdrant_client import QdrantClient

from app.matching.matching_service import MatchingService


class JobMatchRequest(BaseModel):
    job_description: str


def create_matching_router(
    client: QdrantClient,
) -> APIRouter:

    router = APIRouter(
        prefix="/matching",
        tags=["Job Matching"],
    )

    matching_service = MatchingService()

    @router.post("/match")
    def match_resume(
        request: JobMatchRequest,
    ):

        if not request.job_description.strip():
            raise HTTPException(
                status_code=400,
                detail="Job description cannot be empty.",
            )

        try:

            collection_name = "recruitrag_documents"

            points, _ = client.scroll(
                collection_name=collection_name,
                limit=100,
                with_payload=True,
                with_vectors=False,
            )

            if not points:
                raise HTTPException(
                    status_code=404,
                    detail="No indexed resume found.",
                )

            resume_chunks = []

            for point in points:

                payload = point.payload or {}

                text = payload.get("text", "")

                if text:
                    resume_chunks.append(text)

            if not resume_chunks:
                raise HTTPException(
                    status_code=404,
                    detail="Indexed resume contains no text.",
                )

            resume_text = "\n".join(
                resume_chunks
            )

            return matching_service.match_resume_to_job(
                resume_text=resume_text,
                job_description=request.job_description,
            )

        except HTTPException:
            raise

        except Exception as exc:
            raise HTTPException(
                status_code=500,
                detail=f"Job matching failed: {str(exc)}",
            )

    return router