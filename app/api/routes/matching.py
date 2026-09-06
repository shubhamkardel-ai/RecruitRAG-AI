from fastapi import APIRouter
from pydantic import BaseModel

from app.matching.matching_service import MatchingService


class JobMatchRequest(BaseModel):
    resume_text: str
    job_description: str


def create_matching_router() -> APIRouter:

    router = APIRouter(
        prefix="/matching",
        tags=["Job Matching"],
    )

    matching_service = MatchingService()

    @router.post("/match")
    def match_resume(request: JobMatchRequest):

        return matching_service.match_resume_to_job(
            resume_text=request.resume_text,
            job_description=request.job_description,
        )

    return router