from typing import Dict


class JobInterviewer:
    """
    Generates a structured interview prompt
    based on a candidate resume and job description.
    """

    def build_prompt(
        self,
        resume_text: str,
        job_description: str,
    ) -> str:
        """
        Build an AI prompt for generating
        role-specific interview questions.
        """

        if not resume_text.strip():
            raise ValueError(
                "Resume text cannot be empty."
            )

        if not job_description.strip():
            raise ValueError(
                "Job description cannot be empty."
            )

        return f"""
You are an expert technical recruiter.

Analyze the candidate resume against the
provided job description.

Generate a professional interview guide.

Candidate Resume:
-----------------
{resume_text}
-----------------

Job Description:
----------------
{job_description}
----------------

Create the following sections:

1. Technical Interview Questions
   - Ask questions based on the candidate's
     actual technical skills.
   - Focus on skills required by the job.

2. Project-Based Questions
   - Ask questions about projects mentioned
     in the candidate's resume.
   - Focus on implementation, decisions,
     challenges, and results.

3. Experience-Based Questions
   - Ask questions about the candidate's
     professional or internship experience.

4. Skill-Gap Questions
   - Identify important job requirements that
     are missing or weak in the resume.
   - Create questions to evaluate those areas.

5. Behavioral Questions
   - Create recruiter-friendly behavioral
     interview questions.

6. Interviewer Evaluation Points
   - Provide key things the interviewer should
     evaluate in the candidate's answers.

Rules:

- Do not invent candidate experience.
- Do not claim the candidate has a skill
  that is not present in the resume.
- Keep questions specific to the candidate
  and job description.
- Keep the output professional and concise.

Return the interview guide in clear Markdown.
"""

    def validate_input(
        self,
        resume_text: str,
        job_description: str,
    ) -> Dict[str, bool]:
        """
        Validate interview generation inputs.
        """

        return {
            "resume_available": bool(
                resume_text.strip()
            ),
            "job_description_available": bool(
                job_description.strip()
            ),
        }