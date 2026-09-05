class CandidateEvaluator:
    """
    Deterministic recruiter evaluation engine.

    Evaluates resume evidence across six recruiter-focused
    categories. The score is calculated programmatically and
    does not depend on LLM-generated scoring.
    """

    def evaluate(self, candidate_text: str) -> dict:

        if not candidate_text or not candidate_text.strip():
            return {
                "scores": {
                    "technical_skills": 0,
                    "project_experience": 0,
                    "professional_experience": 0,
                    "education": 0,
                    "certifications": 0,
                    "role_relevance": 0,
                },
                "total_score": 0,
                "max_score": 100,
                "recommendation": "Insufficient Evidence",
            }

        text = candidate_text.lower()

        # ==================================================
        # Technical Skills — 20 points
        # ==================================================

        technical_groups = {
            "programming": [
                "python",
                "sql",
            ],
            "data_science": [
                "pandas",
                "numpy",
                "scikit-learn",
                "xgboost",
            ],
            "visualization": [
                "matplotlib",
                "seaborn",
                "tableau",
            ],
            "business_intelligence": [
                "power bi",
                "power query",
                "dax",
                "excel",
            ],
        }

        technical_groups_found = 0
        technical_skill_count = 0

        for skills in technical_groups.values():

            group_found = False

            for skill in skills:

                if skill in text:
                    technical_skill_count += 1
                    group_found = True

            if group_found:
                technical_groups_found += 1

        if (
            technical_skill_count >= 10
            and technical_groups_found >= 4
        ):
            technical_score = 20

        elif (
            technical_skill_count >= 8
            and technical_groups_found >= 3
        ):
            technical_score = 18

        elif (
            technical_skill_count >= 6
            and technical_groups_found >= 3
        ):
            technical_score = 16

        elif (
            technical_skill_count >= 4
            and technical_groups_found >= 2
        ):
            technical_score = 13

        elif technical_skill_count >= 2:
            technical_score = 9

        elif technical_skill_count >= 1:
            technical_score = 5

        else:
            technical_score = 0

        # ==================================================
        # Project Experience — 20 points
        # ==================================================

        project_indicators = [
            "project",
            "dashboard",
            "prediction",
            "analysis",
            "machine learning",
            "exploratory data analysis",
            "eda",
            "feature engineering",
            "model",
            "forecast",
        ]

        project_technology_indicators = [
            "python",
            "pandas",
            "scikit-learn",
            "xgboost",
            "power bi",
            "power query",
            "dax",
            "excel",
            "matplotlib",
            "seaborn",
        ]

        project_indicator_count = sum(
            1
            for indicator in project_indicators
            if indicator in text
        )

        project_technology_count = sum(
            1
            for technology in project_technology_indicators
            if technology in text
        )

        project_names_found = 0

        project_names = [
            "supply chain",
            "production analytics",
            "walmart sales",
            "sales prediction",
        ]

        for project_name in project_names:

            if project_name in text:
                project_names_found += 1

        if (
            project_names_found >= 2
            and project_indicator_count >= 6
            and project_technology_count >= 6
        ):
            project_score = 20

        elif (
            project_names_found >= 2
            and project_indicator_count >= 4
        ):
            project_score = 18

        elif (
            project_names_found >= 1
            and project_indicator_count >= 4
        ):
            project_score = 16

        elif project_indicator_count >= 4:
            project_score = 13

        elif project_indicator_count >= 2:
            project_score = 9

        elif project_indicator_count >= 1:
            project_score = 5

        else:
            project_score = 0

        # ==================================================
        # Professional Experience — 20 points
        # ==================================================

        experience_signals = [
            "business analyst",
            "intern",
            "internship",
            "mis reporting",
            "daily reports",
            "weekly reports",
            "monthly reports",
            "data cleaning",
            "data validation",
            "dashboard",
            "cross-functional",
            "decision-making",
            "business reporting",
        ]

        experience_signal_count = sum(
            1
            for signal in experience_signals
            if signal in text
        )

        has_internship = (
            "intern" in text
            or "internship" in text
        )

        has_business_role = (
            "business analyst" in text
        )

        has_reporting = (
            "mis reporting" in text
            or "business reporting" in text
        )

        has_analytics_work = (
            "data cleaning" in text
            or "data validation" in text
            or "dashboard" in text
        )

        experience_score = 0

        if has_internship:
            experience_score += 6

        if has_business_role:
            experience_score += 4

        if has_reporting:
            experience_score += 3

        if has_analytics_work:
            experience_score += 3

        if experience_signal_count >= 6:
            experience_score += 4

        experience_score = min(
            experience_score,
            20,
        )

        # ==================================================
        # Education — 15 points
        # ==================================================

        has_degree = any(
            term in text
            for term in [
                "b.c.a",
                "bca",
                "bachelor",
                "computer applications",
                "bachelor of computer applications",
            ]
        )

        has_cgpa = "cgpa" in text

        education_score = 0

        if has_degree:
            education_score += 10

        if has_cgpa:
            education_score += 5

        education_score = min(
            education_score,
            15,
        )

        # ==================================================
        # Certifications — 10 points
        # ==================================================

        certification_signals = [
            "certification",
            "python course",
            "data analysis with python",
            "excel tips",
            "power bi virtual internship",
            "data science virtual internship",
            "cognitive class",
            "great learning",
            "cognifyz",
            "saiket",
            "scalar",
        ]

        certification_count = sum(
            1
            for signal in certification_signals
            if signal in text
        )

        if certification_count >= 5:
            certification_score = 10

        elif certification_count >= 4:
            certification_score = 9

        elif certification_count >= 3:
            certification_score = 7

        elif certification_count >= 2:
            certification_score = 5

        elif certification_count >= 1:
            certification_score = 3

        else:
            certification_score = 0

        # ==================================================
        # Role Relevance — 15 points
        # ==================================================

        role_signals = [
            "data analyst",
            "business analyst",
            "data scientist",
            "data analytics",
            "machine learning",
            "business intelligence",
            "predictive analytics",
            "data analysis",
        ]

        role_signal_count = sum(
            1
            for signal in role_signals
            if signal in text
        )

        analytics_stack_present = (
            "python" in text
            and (
                "pandas" in text
                or "scikit-learn" in text
            )
        )

        bi_stack_present = (
            "power bi" in text
            and "excel" in text
        )

        project_evidence_present = (
            project_names_found >= 1
        )

        role_score = 0

        if role_signal_count >= 5:
            role_score += 7

        elif role_signal_count >= 3:
            role_score += 5

        elif role_signal_count >= 1:
            role_score += 3

        if analytics_stack_present:
            role_score += 3

        if bi_stack_present:
            role_score += 2

        if project_evidence_present:
            role_score += 3

        role_score = min(
            role_score,
            15,
        )

        # ==================================================
        # Final Scores
        # ==================================================

        scores = {
            "technical_skills": technical_score,
            "project_experience": project_score,
            "professional_experience": experience_score,
            "education": education_score,
            "certifications": certification_score,
            "role_relevance": role_score,
        }

        total_score = sum(
            scores.values()
        )

        # ==================================================
        # Recruiter Recommendation
        # ==================================================

        if total_score >= 80:
            recommendation = "Strong Fit"

        elif total_score >= 65:
            recommendation = "Potential Fit"

        elif total_score >= 50:
            recommendation = "Needs Review"

        else:
            recommendation = "Weak Fit"

        return {
            "scores": scores,
            "total_score": total_score,
            "max_score": 100,
            "recommendation": recommendation,
        }