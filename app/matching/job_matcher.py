
from typing import Dict, List


class JobMatcher:
    """Compares a candidate resume against a job description."""

    def match(
        self,
        resume_text: str,
        job_description: str,
    ) -> Dict:
        """Perform basic skill-based job matching."""

        if not resume_text.strip() or not job_description.strip():
            return {
                "match_score": 0,
                "matching_skills": [],
                "missing_skills": [],
            }

        resume_lower = resume_text.lower()
        job_lower = job_description.lower()

        skills = self._extract_skills(job_lower)

        matching_skills = [
            skill for skill in skills if skill in resume_lower
        ]
        missing_skills = [
            skill for skill in skills if skill not in resume_lower
        ]

        score = (
            round(len(matching_skills) / len(skills) * 100)
            if skills else 0
        )

        return {
            "match_score": score,
            "matching_skills": matching_skills,
            "missing_skills": missing_skills,
        }

    @staticmethod
    def _extract_skills(job_description: str) -> List[str]:
        """Find known skills mentioned in a job description."""

        skill_dictionary = [
            "python", "sql", "java", "c++", "javascript", "typescript",
            "go", "rust", "pandas", "numpy", "scikit-learn", "pytorch",
            "tensorflow", "opencv", "matplotlib", "seaborn",
            "machine learning", "deep learning", "data science",
            "data analysis", "data preprocessing", "feature engineering",
            "model evaluation", "natural language processing",
            "computer vision", "xgboost", "langchain", "rag", "llm",
            "generative ai", "prompt engineering", "ai agents",
            "fastapi", "django", "flask", "rest api", "rest apis",
            "api integration", "mysql", "postgresql", "mongodb", "qdrant",
            "redis", "aws", "aws eks", "azure", "gcp", "cloud deployment",
            "docker", "kubernetes", "terraform", "helm", "service mesh",
            "incident management", "production incident management",
            "ci/cd", "github actions", "linux", "git", "github",
            "power bi", "tableau", "excel", "power query", "dax",
            "unit testing", "automated testing",
            "data structures and algorithms", "system design",
        ]

        found_skills = [
            skill for skill in skill_dictionary
            if skill in job_description
        ]

        # Remove duplicate matches and check longer phrases first.
        return sorted(
            set(found_skills),
            key=lambda skill: (-len(skill), job_description.find(skill)),
        )
