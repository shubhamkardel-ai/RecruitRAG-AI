import os
import requests
import streamlit as st


# ==========================================================
# Configuration
# ==========================================================

API_URL = os.getenv(
    "API_URL",
    "http://127.0.0.1:8000"
)

# ==========================================================
# Page Configuration
# ==========================================================

st.set_page_config(
    page_title="RecruitRAG-AI",
    page_icon="🤖",
    layout="wide",
)

if "resume_indexed" not in st.session_state:
    st.session_state.resume_indexed = False

if "candidate_evaluation" not in st.session_state:
    st.session_state.candidate_evaluation = None

# ==========================================================
# Application Header
# ==========================================================

st.title("🤖 RecruitRAG-AI")

st.subheader("⚡ AI-Powered Recruitment Intelligence Platform")

st.caption(
    "AI-powered recruitment intelligence • "
    "Resume understanding • Candidate evaluation"
)

st.divider()

status_col1, status_col2, status_col3 = st.columns(3)

with status_col1:

    try:

        health_response = requests.get(
            f"{API_URL}/health",
            timeout=5,
        )

        if health_response.status_code == 200:
            st.success("🟢 API Connected")
        else:
            st.error("🔴 API Offline")

    except requests.exceptions.RequestException:

        st.error("🔴 API Offline")

with status_col2:
    st.info("🔵 RAG Engine Active")

with status_col3:
    st.info("🔵 AI Assistant Active")

st.divider()

# ==========================================================
# Recruiter Workspace
# ==========================================================

left_col, right_col = st.columns(
    [1, 1.4],
    gap="large",
)


# ==========================================================
# Candidate Resume
# ==========================================================

with left_col:

    st.subheader("📄 AI-Powered Resume Analysis")

    st.caption(
        "Upload a candidate resume to unlock AI-powered recruitment insights."
    )

    uploaded_file = st.file_uploader(
        "📎 Drop candidate resume here",
        type=["pdf", "docx", "txt"],
        help="Supported formats: PDF, DOCX, TXT",
    )

    if uploaded_file is not None:

        st.success(
            f"Resume ready: {uploaded_file.name}"
        )

        file_size_kb = uploaded_file.size / 1024

        st.caption(
            f"File type: {uploaded_file.type} • "
            f"Size: {file_size_kb:.1f} KB"
        )

        # --------------------------------------------------
        # Index Resume
        # --------------------------------------------------

        if st.button(
            "🚀 Index Resume",
            use_container_width=True,
            type="primary",
        ):

            try:

                with st.spinner("Processing resume..."):

                    response = requests.post(
                        f"{API_URL}/documents/upload",
                        files={
                            "file": (
                                uploaded_file.name,
                                uploaded_file.getvalue(),
                            )
                        },
                        timeout=120,
                    )

                if response.status_code == 200:

                    st.success(
                        "✅ Resume indexed successfully."
                    )

                    upload_data = response.json()

                    st.session_state.resume_indexed = True
                    st.session_state.candidate_evaluation = upload_data.get(
                        "evaluation"
                    )

                    evaluation = st.session_state.candidate_evaluation

                    if evaluation:

                        st.subheader("🎯 Candidate Evaluation")

                        score_col1, score_col2 = st.columns(2)

                        with score_col1:
                            st.metric(
                                "Overall Score",
                                f"{evaluation['total_score']}/{evaluation['max_score']}",
                            )

                            st.caption(
                                "Overall candidate fit score"
                            )

                        with score_col2:
                            st.metric(
                                "Recommendation",
                                evaluation["recommendation"],
                            )

                            if evaluation["recommendation"] == "Strong Fit":
                                st.caption("High alignment with the evaluated resume evidence.")

                            elif evaluation["recommendation"] == "Potential Fit":
                                st.caption("Good potential with some areas requiring review.")

                            elif evaluation["recommendation"] == "Needs Review":
                                st.caption("Additional recruiter review is recommended.")

                            else:
                                st.caption("Limited evidence of alignment with the evaluated role.")

                        st.caption(
                            "AI-assisted candidate evaluation based on resume evidence."
                        )

                        st.markdown("#### 📊 Evaluation Breakdown")

                        st.caption(
                            "Resume-based scoring across technical capability, experience, education, "
                            "certifications, and role relevance."
                        )

                        scores = evaluation["scores"]

                        for category, score in scores.items():
                            label = category.replace("_", " ").title()

                            max_score = {
                                "technical_skills": 20,
                                "project_experience": 20,
                                "professional_experience": 20,
                                "education": 15,
                                "certifications": 10,
                                "role_relevance": 15,
                            }[category]

                            st.write(
                                f"**{label}** — {score}/{max_score}"
                            )

                            st.progress(
                                score / {
                                    "technical_skills": 20,
                                    "project_experience": 20,
                                    "professional_experience": 20,
                                    "education": 15,
                                    "certifications": 10,
                                    "role_relevance": 15,
                                }[category]
                            )

                else:

                    st.error(
                        f"Upload failed: {response.status_code}"
                    )

            except requests.exceptions.ConnectionError:

                st.error(
                    "FastAPI is not running."
                )

            except requests.exceptions.Timeout:

                st.error(
                    "The upload request timed out."
                )

        # --------------------------------------------------
        # AI Candidate Summary
        # --------------------------------------------------

        if st.session_state.resume_indexed:

            if st.button(
                "✨ Generate AI Candidate Summary",
                use_container_width=True,
            ):

                try:

                    with st.spinner(
                        "Generating AI candidate summary..."
                    ):

                        summary_response = requests.post(
                            f"{API_URL}/chat/ask",
                            json={
                                "question": (
                                    "Generate a professional recruiter-ready "
                                    "candidate summary. Include candidate "
                                    "overview, experience, technical skills, "
                                    "projects, education, key strengths, "
                                    "potential gaps, recommended role, and "
                                    "overall recruiter assessment. Use only "
                                    "information available in the uploaded resume."
                                )
                            },
                            timeout=120,
                        )

                    if summary_response.status_code == 200:

                        summary_data = summary_response.json()

                        st.subheader(
                            "✨ AI Candidate Summary"
                        )

                        st.info(
                            summary_data["answer"]
                        )

                    else:

                        st.error(
                            f"Summary generation failed: "
                            f"{summary_response.status_code}"
                        )

                except requests.exceptions.ConnectionError:

                    st.error(
                        "FastAPI is not running."
                    )

                except requests.exceptions.Timeout:

                    st.error(
                        "The summary request timed out."
                    )
# ==========================================================
# Recruiter Intelligence
# ==========================================================

with right_col:

    st.subheader("💬 Recruiter Intelligence")

    st.caption(
        "Ask natural-language questions about the candidate."
    )

    analysis_mode = st.selectbox(
        "AI Analysis Mode",
        [
            "Recruiter Q&A",
            "Candidate Strengths",
            "Technical Skills",
            "Project Experience",
            "Recruiter Recommendation",
            "Interview Focus Areas",
        ],
    )

    if analysis_mode == "Recruiter Q&A":

        question = st.text_area(
            "Recruiter Question",
            placeholder="Ask anything about the candidate...",
            height=100,
        )

    else:

        question = st.text_area(
            "Recruiter Question",
            value=f"Analyze the candidate's {analysis_mode.lower()}.",
            height=100,
        )

    st.caption(
        "Try asking:"
    )

    st.write(
        "• What are the candidate's strongest technical skills?\n"
        "• What AI/ML projects has the candidate built?\n"
        "• Does the candidate have Python experience?"
    )

    if st.button(
            "🧠 Analyze Candidate",
            use_container_width=True,
            type="primary",
    ):

        if not question.strip():

            st.warning(
                "Please enter a question."
            )

        else:

            try:

                with st.spinner(
                    "Analyzing candidate..."
                ):

                    response = requests.post(
                        f"{API_URL}/chat/ask",
                        json={
                            "question": (
                                f"AI Analysis Mode: {analysis_mode}\n\n"
                                f"Recruiter Question: {question}"
                            )
                        },
                        timeout=120,
                    )

                if response.status_code == 200:

                    data = response.json()

                    st.subheader(
                        f"🎯 AI {analysis_mode} Insight"
                    )

                    st.info(
                        data["answer"]
                    )

                else:

                    st.error(
                        f"API error: {response.status_code}"
                    )

            except requests.exceptions.ConnectionError:

                st.error(
                    "FastAPI is not running."
                )

            except requests.exceptions.Timeout:

                st.error(
                    "The request timed out."
                )

# ==========================================================
# Footer
# ==========================================================

st.divider()

st.caption(
    "RecruitRAG-AI · Intelligent Resume Screening & Candidate Insights"
)