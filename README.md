<div align="center">

# 🤖 RecruitRAG-AI

### AI-Powered Recruitment Intelligence Platform

**Resume Understanding • Candidate Evaluation • RAG • Job Matching • Interview Intelligence**

<br>

[![Live Demo](https://img.shields.io/badge/🚀_Live_Demo-RecruitRAG--AI-00F7FF?style=for-the-badge)](https://recruitrag-ai-szgzxyf5eum4c9lg4xtvxq.streamlit.app/)
[![GitHub](https://img.shields.io/badge/GitHub-Repository-181717?style=for-the-badge&logo=github)](https://github.com/shubhamkardel-ai/RecruitRAG-AI)
[![Python](https://img.shields.io/badge/Python-3.12+-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-Backend-009688?style=for-the-badge&logo=fastapi&logoColor=white)](https://fastapi.tiangolo.com/)
[![Streamlit](https://img.shields.io/badge/Streamlit-Frontend-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)](https://streamlit.io/)

</div>

---

## 🧠 Overview

**RecruitRAG-AI** is an AI-powered recruitment intelligence platform designed to help recruiters understand, evaluate, and interact with candidate resumes using modern AI and Retrieval-Augmented Generation (RAG).

Instead of treating a resume as a static document, RecruitRAG-AI transforms it into a searchable candidate knowledge base and provides multiple recruiter-focused intelligence capabilities.

### RecruitRAG-AI can:

- 📄 Understand uploaded resumes
- 🧠 Store resume knowledge using vector embeddings
- 🔎 Retrieve relevant candidate information using RAG
- 🎯 Evaluate candidates using structured scoring
- 📊 Break down candidate strengths across multiple dimensions
- 🧩 Compare candidates against job descriptions
- ⚠️ Identify missing or weak skills
- 🎤 Generate role-specific interview questions
- 💬 Answer recruiter questions using candidate evidence

---

# 🚀 Live Application

### 🌐 Try RecruitRAG-AI

**Live Demo**

👉 https://recruitrag-ai-szgzxyf5eum4c9lg4xtvxq.streamlit.app/

**Backend API**

👉 https://recruitrag-ai-api.onrender.com

---

# ✨ Core Capabilities

## 1. 📄 AI-Powered Resume Analysis

RecruitRAG-AI supports:

- PDF
- DOCX
- TXT

Resume documents are processed through an ingestion pipeline and transformed into searchable chunks.

Each document is:

```text
Resume
   ↓
Document Loader
   ↓
Text Extraction
   ↓
Chunking
   ↓
Embedding Generation
   ↓
Qdrant Vector Database
   ↓
Retrieval
   ↓
AI Analysis
