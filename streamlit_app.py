import os
import html
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


# ==========================================================
# Session State
# ==========================================================

if "resume_indexed" not in st.session_state:
    st.session_state.resume_indexed = False

if "candidate_evaluation" not in st.session_state:
    st.session_state.candidate_evaluation = None

if "hiring_insights" not in st.session_state:
    st.session_state.hiring_insights = None

if "candidate_summary" not in st.session_state:
    st.session_state.candidate_summary = None

if "job_match" not in st.session_state:
    st.session_state.job_match = None

if "interview_guide" not in st.session_state:
    st.session_state.interview_guide = None


# ==========================================================
# Application Header
# ==========================================================

st.title("🤖 RecruitRAG-AI")

st.subheader(
    "⚡ AI-Powered Recruitment Intelligence Platform"
)

st.caption(
    "AI-powered recruitment intelligence • "
    "Resume understanding • Candidate evaluation"
)

st.divider()


# ==========================================================
# System Status
# ==========================================================

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
# LEFT COLUMN
# Candidate Resume
# ==========================================================

with left_col:

    st.subheader(
        "📄 AI-Powered Resume Analysis"
    )

    st.caption(
        "Upload a candidate resume to unlock "
        "AI-powered recruitment insights."
    )

    uploaded_file = st.file_uploader(
        "📎 Drop candidate resume here",
        type=["pdf", "docx", "txt"],
        help="Supported formats: PDF, DOCX, TXT",
    )


    # ======================================================
    # Resume Uploaded
    # ======================================================

    if uploaded_file is not None:

        st.success(
            f"Resume ready: {uploaded_file.name}"
        )

        file_size_kb = uploaded_file.size / 1024

        st.caption(
            f"File type: {uploaded_file.type} • "
            f"Size: {file_size_kb:.1f} KB"
        )


        # ==================================================
        # Index Resume
        # ==================================================

        if st.button(
            "🚀 Index Resume",
            use_container_width=True,
            type="primary",
        ):

            try:

                with st.spinner(
                    "Processing resume..."
                ):

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

                    st.session_state.candidate_evaluation = (
                        upload_data.get("evaluation")
                    )

                    evaluation = (
                        st.session_state.candidate_evaluation
                    )

                else:

                    st.error(
                        f"Upload failed: "
                        f"{response.status_code}"
                    )


            except requests.exceptions.ConnectionError:

                st.error(
                    "FastAPI is not running."
                )

            except requests.exceptions.Timeout:

                st.error(
                    "The upload request timed out."
                )


    # ======================================================
    # Recruiter Decision
    # ======================================================

    if st.session_state.resume_indexed:

        evaluation = (
            st.session_state.candidate_evaluation
        )

        if evaluation:

            st.subheader(
                "🎯 Recruiter Decision"
            )

            st.caption(
                "AI-assisted candidate evaluation "
                "based on evidence extracted from "
                "the uploaded resume."
            )

            decision_col1, decision_col2 = (
                st.columns(2)
            )

            with decision_col1:

                st.markdown(
                    f'<div style="background:#111820;border:1px solid #00E5FF;border-radius:12px;padding:18px;text-align:center;"><div style="font-size:13px;color:#A7B0BA;margin-bottom:8px;">Overall Candidate Score</div><div style="font-size:32px;font-weight:700;color:#00E5FF;">{evaluation["total_score"]}/{evaluation["max_score"]}</div></div>',
                    unsafe_allow_html=True,
                )

            with decision_col2:

                st.markdown(
                    f'<div style="background:#111820;border:1px solid #00E5FF;border-radius:12px;padding:18px;text-align:center;"><div style="font-size:13px;color:#A7B0BA;margin-bottom:8px;">Hiring Recommendation</div><div style="font-size:26px;font-weight:700;color:#00E5FF;">{evaluation["recommendation"]}</div></div>',
                    unsafe_allow_html=True,
                )


            if evaluation["recommendation"] == "Strong Fit":

                st.success(
                    "✅ Strong alignment with the "
                    "evaluated role and resume evidence."
                )

            elif evaluation["recommendation"] == "Potential Fit":

                st.warning(
                    "🟡 Candidate shows good potential "
                    "but requires additional review."
                )

            elif evaluation["recommendation"] == "Needs Review":

                st.warning(
                    "🟠 Additional recruiter review "
                    "is recommended."
                )

            else:

                st.error(
                    "🔴 Limited evidence of alignment "
                    "with the evaluated role."
                )


            # ==================================================
            # Evaluation Breakdown
            # ==================================================

            st.markdown(
                "#### 📊 Evaluation Breakdown"
            )

            st.caption(
                "Candidate score across technical capability, "
                "project experience, professional experience, "
                "education, certifications, and role relevance."
            )

            scores = evaluation["scores"]

            max_scores = {
                "technical_skills": 20,
                "project_experience": 20,
                "professional_experience": 20,
                "education": 15,
                "certifications": 10,
                "role_relevance": 15,
            }

            score_col1, score_col2 = (
                st.columns(2)
            )

            score_items = list(
                scores.items()
            )

            for index, (
                category,
                score,
            ) in enumerate(score_items):

                max_score = max_scores[category]

                label = (
                    category
                    .replace("_", " ")
                    .title()
                )

                target_col = (
                    score_col1
                    if index % 2 == 0
                    else score_col2
                )

                with target_col:

                    st.write(
                        f"**{label}**"
                    )

                    progress_percentage = (
                        score / max_score
                    ) * 100

                    st.markdown(
                        f"""
                        <div style="
                            width:100%;
                            height:6px;
                            background:#151A21;
                            border-radius:10px;
                            overflow:hidden;
                            margin:8px 0 12px 0;
                        ">
                            <div style="
                                width:{progress_percentage}%;
                                height:100%;
                                background:#00E5FF;
                                border-radius:10px;
                            "></div>
                        </div>
                        """,
                        unsafe_allow_html=True,
                    )

                    st.markdown(
                        f"""
                        <div style="
                            text-align:right;
                            margin-top:-4px;
                            margin-bottom:12px;
                            font-size:13px;
                            font-weight:600;
                            color:#00E5FF;
                        ">
                            {score}/{max_score}
                        </div>
                        """,
                        unsafe_allow_html=True,
                    )


            # ==================================================
            # AI Hiring Insights
            # ==================================================

            st.markdown(
                "#### 🧠 AI Hiring Insights"
            )

            st.caption(
                "Generate a recruiter-ready assessment "
                "using the indexed candidate resume."
            )

            if st.button(
                "🧠 Generate Recruiter Hiring Insights",
                use_container_width=True,
            ):

                try:

                    with st.spinner(
                        "Generating recruiter hiring insights..."
                    ):

                        insight_response = requests.post(
                            f"{API_URL}/chat/ask",
                            json={
                                "question": (
                                    "Generate a concise recruiter "
                                    "hiring assessment using only "
                                    "the uploaded candidate resume. "
                                    "Include key strengths, "
                                    "potential skill gaps, "
                                    "recommended role, "
                                    "interview focus areas, "
                                    "and final hiring assessment. "
                                    "Keep the response professional "
                                    "and recruiter-ready."
                                )
                            },
                            timeout=120,
                        )


                    if insight_response.status_code == 200:

                        insight_data = (
                            insight_response.json()
                        )

                        st.session_state.hiring_insights = (
                            insight_data["answer"]
                        )

                        st.success(
                            "✅ Hiring insights generated."
                        )

                    else:

                        st.error(
                            "Hiring insight generation failed: "
                            f"{insight_response.status_code}"
                        )


                except requests.exceptions.ConnectionError:

                    st.error(
                        "FastAPI is not running."
                    )

                except requests.exceptions.Timeout:

                    st.error(
                        "The hiring insight request timed out."
                    )


            if st.session_state.hiring_insights:

                insight_text = html.escape(
                    st.session_state.hiring_insights
                )

                st.markdown(
                    f"""
                    <div style="
                        background:#111820;
                        border:1px solid #00E5FF;
                        border-radius:12px;
                        padding:20px;
                        margin-top:12px;
                    ">
                        <div style="
                            font-size:14px;
                            font-weight:700;
                            color:#00E5FF;
                            margin-bottom:12px;
                        ">
                            🧠 Recruiter Assessment
                        </div>

                        <div style="
                            color:#E6EDF3;
                            font-size:14px;
                            line-height:1.7;
                            white-space:pre-wrap;
                        ">
                            {insight_text}
                        </div>
                    </div>
                    """,
                    unsafe_allow_html=True,
                )


            # ==================================================
            # AI Candidate Summary
            # ==================================================

            st.divider()

            st.subheader(
                "✨ AI Candidate Summary"
            )

            st.caption(
                "Generate a recruiter-ready summary "
                "from the indexed candidate resume."
            )

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
                                    "Generate a professional "
                                    "recruiter-ready candidate "
                                    "summary. Include candidate "
                                    "overview, experience, "
                                    "technical skills, projects, "
                                    "education, key strengths, "
                                    "potential gaps, recommended "
                                    "role, and overall recruiter "
                                    "assessment. Use only "
                                    "information available in "
                                    "the uploaded resume."
                                )
                            },
                            timeout=120,
                        )


                    if summary_response.status_code == 200:

                        summary_data = (
                            summary_response.json()
                        )

                        st.session_state.candidate_summary = (
                            summary_data["answer"]
                        )

                        st.success(
                            "✅ Candidate summary generated."
                        )

                    else:

                        st.error(
                            "Summary generation failed: "
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


            if st.session_state.candidate_summary:

                st.info(
                    st.session_state.candidate_summary
                )


            # ==================================================
            # Job Description Matching
            # ==================================================

            st.divider()

            st.subheader(
                "🎯 Job Description Matching"
            )

            st.caption(
                "Compare the indexed candidate resume "
                "against a target job description."
            )

            job_description = st.text_area(
                "📋 Paste Job Description",
                placeholder=(
                    "Paste the target job description here..."
                ),
                height=180,
            )

            if st.button(
                "🔍 Analyze Job Match",
                use_container_width=True,
                type="primary",
            ):

                if not job_description.strip():

                    st.warning(
                        "Please paste a job description."
                    )

                else:

                    try:

                        with st.spinner(
                            "Analyzing candidate-job match..."
                        ):

                            match_response = requests.post(
                                f"{API_URL}/matching/match",
                                json={
                                    "job_description":
                                        job_description,
                                },
                                timeout=120,
                            )


                        if match_response.status_code == 200:

                            match_data = (
                                match_response.json()
                            )

                            st.session_state.job_match = (
                                match_data
                            )

                            st.success(
                                "✅ Job match analysis completed."
                            )

                        else:

                            st.error(
                                "Job matching failed: "
                                f"{match_response.status_code}"
                            )


                    except requests.exceptions.ConnectionError:

                        st.error(
                            "FastAPI is not running."
                        )

                    except requests.exceptions.Timeout:

                        st.error(
                            "The job matching request timed out."
                        )


            if st.session_state.job_match:

                match_data = (
                    st.session_state.job_match
                )

                st.metric(
                    "Job Match Score",
                    f"{match_data['match_score']}%",
                )

                st.markdown(
                    "#### ✅ Matching Skills"
                )

                if match_data["matching_skills"]:

                    st.write(
                        ", ".join(
                            match_data["matching_skills"]
                        )
                    )

                else:

                    st.caption(
                        "No matching skills identified."
                    )

                st.markdown(
                    "#### ⚠️ Missing Skills"
                )

                if match_data["missing_skills"]:

                    st.write(
                        ", ".join(
                            match_data["missing_skills"]
                        )
                    )

                else:

                    st.success(
                        "No major missing skills identified."
                    )


            # ==================================================
            # AI Interview Intelligence
            # ==================================================

            st.divider()

            st.subheader(
                "🤖 AI Interview Intelligence"
            )

            st.caption(
                "Generate role-specific interview questions "
                "from the candidate resume and job description."
            )

            interview_job_description = st.text_area(
                "📋 Paste Job Description for Interview",
                placeholder=(
                    "Paste the target job description here..."
                ),
                height=180,
            )

            if st.button(
                "🎤 Generate Interview Guide",
                use_container_width=True,
                type="primary",
            ):

                if not interview_job_description.strip():

                    st.warning(
                        "Please paste a job description."
                    )

                else:

                    try:

                        with st.spinner(
                            "Generating AI interview guide..."
                        ):

                            interview_response = requests.post(
                                f"{API_URL}/interview/generate",
                                json={
                                    "job_description":
                                        interview_job_description,
                                },
                                timeout=180,
                            )


                        if interview_response.status_code == 200:

                            interview_data = (
                                interview_response.json()
                            )

                            st.session_state.interview_guide = (
                                interview_data[
                                    "interview_guide"
                                ]
                            )

                            st.success(
                                "✅ Interview guide generated successfully."
                            )

                        else:

                            st.error(
                                "Interview generation failed: "
                                f"{interview_response.status_code}"
                            )


                    except requests.exceptions.ConnectionError:

                        st.error(
                            "FastAPI is not running."
                        )

                    except requests.exceptions.Timeout:

                        st.error(
                            "The interview generation request "
                            "timed out."
                        )


            if st.session_state.interview_guide:

                st.markdown(
                    "#### 🎤 Generated Interview Guide"
                )

                st.markdown(
                    st.session_state.interview_guide
                )


# ==========================================================
# RIGHT COLUMN
# Recruiter Intelligence
# ==========================================================

with right_col:

    st.subheader(
        "💬 Recruiter Intelligence"
    )

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
            placeholder=(
                "Ask anything about the candidate..."
            ),
            height=100,
        )

    else:

        question = st.text_area(
            "Recruiter Question",
            value=(
                f"Analyze the candidate's "
                f"{analysis_mode.lower()}."
            ),
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
                                f"AI Analysis Mode: "
                                f"{analysis_mode}\n\n"
                                f"Recruiter Question: "
                                f"{question}"
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
                        f"API error: "
                        f"{response.status_code}"
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
    "RecruitRAG-AI · Intelligent Resume Screening "
    "& Candidate Insights"
)