from typing import Dict, List


class JobMatcher:
    """
    Compares a candidate resume against a job description.
    """

    def match(
        self,
        resume_text: str,
        job_description: str,
    ) -> Dict:
        """
        Perform a basic skill-based job matching analysis.
        """

        if not resume_text.strip():
            return {
                "match_score": 0,
                "matching_skills": [],
                "missing_skills": [],
            }

        if not job_description.strip():
            return {
                "match_score": 0,
                "matching_skills": [],
                "missing_skills": [],
            }

        resume_lower = resume_text.lower()
        job_lower = job_description.lower()

        skills = self._extract_skills(job_lower)

        matching_skills: List[str] = []
        missing_skills: List[str] = []

        for skill in skills:

            if skill.lower() in resume_lower:
                matching_skills.append(skill)

            else:
                missing_skills.append(skill)

        if skills:

            match_score = round(
                (len(matching_skills) / len(skills)) * 100
            )

        else:

            match_score = 0

        return {
            "match_score": match_score,
            "matching_skills": matching_skills,
            "missing_skills": missing_skills,
        }


    def _extract_skills(
        self,
        job_description: str,
    ) -> List[str]:
        """
        Extract commonly used technical skills
        from a job description.
        """

        skill_dictionary = [
            "python",
            "sql",
            "java",
            "c++",
            "javascript",
            "typescript",
            "pandas",
            "numpy",
            "scikit-learn",
            "pytorch",
            "tensorflow",
            "opencv",
            "matplotlib",
            "seaborn",
            "power bi",
            "tableau",
            "excel",
            "power query",
            "dax",
            "fastapi",
            "django",
            "flask",
            "langchain",
            "rag",
            "llm",
            "generative ai",
            "machine learning",
            "deep learning",
            "data science",
            "data analysis",
            "git",
            "github",
            "docker",
            "aws",
            "azure",
            "gcp",
        ]

        return [
            skill
            for skill in skill_dictionary
            if skill in job_description
        ]