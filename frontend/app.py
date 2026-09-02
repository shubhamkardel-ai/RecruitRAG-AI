import requests
import streamlit as st

# ==========================================================
# Configuration
# ==========================================================

API_URL = "http://127.0.0.1:8000"

# ==========================================================
# Page Configuration
# ==========================================================

st.set_page_config(
    page_title="RecruitRAG-AI",
    page_icon="🤖",
    layout="wide",
)

# ==========================================================
# Header
# ==========================================================

st.title("🤖 RecruitRAG-AI")
st.subheader("AI-Powered Recruitment Intelligence")

st.write(
    "Upload resumes and ask questions using Retrieval-Augmented Generation."
)

# ==========================================================
# Resume Upload
# ==========================================================

st.markdown("### 📄 Upload Resume")

uploaded_file = st.file_uploader(
    "Choose a resume PDF",
    type=["pdf"],
)

if uploaded_file is not None:

    if st.button("📤 Upload Resume"):

        files = {
            "file": (
                uploaded_file.name,
                uploaded_file.getvalue(),
                "application/pdf",
            )
        }

        try:
            response = requests.post(
                f"{API_URL}/documents/upload",
                files=files,
                timeout=120,
            )

            if response.status_code == 200:
                result = response.json()

                st.success("Resume uploaded successfully!")

                st.json(result)

            else:
                st.error(
                    f"Upload failed: HTTP {response.status_code}"
                )
                st.code(response.text)

        except requests.exceptions.RequestException as error:
            st.error(f"Could not connect to FastAPI: {error}")


# ==========================================================
# Recruiter Chat
# ==========================================================

st.markdown("---")
st.markdown("### 💬 Recruiter Chat")

question = st.text_input(
    "Ask a question about the candidate",
    placeholder="e.g. What technical skills does the candidate have?",
)

if st.button("🔍 Ask RecruitRAG-AI"):

    if not question.strip():
        st.warning("Please enter a question.")

    else:
        try:
            response = requests.post(
                f"{API_URL}/chat/ask",
                json={"question": question},
                timeout=120,
            )

            if response.status_code == 200:
                result = response.json()

                st.markdown("#### 🤖 AI Response")
                st.write(result["answer"])

            else:
                st.error(
                    f"Request failed: HTTP {response.status_code}"
                )
                st.code(response.text)


        except requests.exceptions.RequestException as error:

            st.error(

                f"Could not connect to FastAPI: {error}"

            )