from app.generation.llm import LLMService
from app.interview.job_interviewer import JobInterviewer


class InterviewService:
    """
    Service responsible for generating
    AI-powered interview guides.
    """

    def __init__(self):
        self.interviewer = JobInterviewer()
        self.llm = LLMService()

    def generate_interview(
        self,
        resume_text: str,
        job_description: str,
    ) -> str:
        """
        Generate an interview guide using
        the candidate resume and job description.
        """

        prompt = self.interviewer.build_prompt(
            resume_text=resume_text,
            job_description=job_description,
        )

        return self.llm.generate(
            prompt=prompt
        )