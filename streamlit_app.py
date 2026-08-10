import requests
import streamlit as st

st.set_page_config(
    page_title="RecruitRAG-AI",
    page_icon="🤖",
    layout="wide",
)

st.title("🤖 RecruitRAG-AI")
st.subheader("AI-Powered Recruitment RAG System")

st.write(
    "Ask questions about the candidate using the indexed resume."
)

st.divider()

st.header("💬 Ask RecruitRAG-AI")

question = st.text_input(
    "Enter your question",
    placeholder="What AI projects has the candidate built?",
)

if st.button("Ask RecruitRAG-AI"):
    if not question.strip():
        st.warning("Please enter a question.")
    else:
        try:
            response = requests.post(
                "http://127.0.0.1:8000/ask",
                json={"question": question},
                timeout=60,
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
                "FastAPI is not running. Start the API first."
            )