import os
import requests
import streamlit as st

API_URL = os.getenv("API_URL", "http://127.0.0.1:8000")

st.set_page_config(
    page_title="RecruitRAG-AI",
    page_icon="🤖",
    layout="wide",
)

st.title("🤖 RecruitRAG-AI")
st.subheader("AI-Powered Recruitment RAG System")

st.write(
    "Upload a candidate resume and ask questions "
    "using Retrieval-Augmented Generation."
)

st.divider()

# ==========================================================
# Resume Upload
# ==========================================================

st.header("📄 Upload Candidate Resume")

uploaded_file = st.file_uploader(
    "Upload PDF, DOCX, or TXT",
    type=["pdf", "docx", "txt"],
)

if uploaded_file is not None:

    if st.button("📥 Index Resume"):

        try:
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

                data = response.json()

                st.success(
                    f"✅ {uploaded_file.name} indexed successfully!"
                )

                st.json(data)

            else:
                st.error(
                    f"Upload failed: {response.status_code}"
                )

        except requests.exceptions.ConnectionError:
            st.error(
                "FastAPI is not running. "
                "Please start the backend first."
            )

# ==========================================================
# Question Answering
# ==========================================================

st.divider()

st.header("💬 Ask RecruitRAG-AI")

question = st.text_input(
    "Enter your question",
    placeholder="What AI projects has the candidate built?",
)

if st.button("🔍 Ask RecruitRAG-AI"):

    if not question.strip():

        st.warning("Please enter a question.")

    else:

        try:

            response = requests.post(
                f"{API_URL}/chat/ask",
                json={
                    "question": question
                },
                timeout=120,
            )

            if response.status_code == 200:

                data = response.json()

                st.success("Answer")

                st.write(data["answer"])

            else:

                st.error(
                    f"API error: {response.status_code}"
                )

        except requests.exceptions.ConnectionError:

            st.error(
                "FastAPI is not running. "
                "Please start the backend first."
            )