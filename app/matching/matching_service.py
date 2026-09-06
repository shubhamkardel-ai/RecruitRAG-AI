from app.matching.job_matcher import JobMatcher


class MatchingService:
    """
    Service responsible for matching a candidate resume
    against a job description.
    """

    def __init__(self):
        self.matcher = JobMatcher()

    def match_resume_to_job(
        self,
        resume_text: str,
        job_description: str,
    ) -> dict:
        """
        Compare resume content with a job description.
        """

        return self.matcher.match(
            resume_text=resume_text,
            job_description=job_description,
        )