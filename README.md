::: {align="center"}
`<img src="https://capsule-render.vercel.app/api?type=waving&color=0:020617,25:061A3A,55:0B3B60,80:007C91,100:00F7FF&height=280&section=header&text=RecruitRAG-AI&fontSize=62&fontColor=FFFFFF&fontAlignY=38&desc=AI-Powered%20Recruitment%20Intelligence%20Platform&descAlignY=58&descSize=20&animation=fadeIn" width="100%"/>`{=html}

`<a href="https://recruitrag-ai-szgzxyf5eum4c9lg4xtvxq.streamlit.app/">`{=html}
`<img src="https://img.shields.io/badge/%F0%9F%9A%80_Live_Demo-RecruitRAG--AI-00F7FF?style=for-the-badge" alt="Live Demo"/>`{=html}
`</a>`{=html}
`<a href="https://recruitrag-ai-api.onrender.com/docs">`{=html}
`<img src="https://img.shields.io/badge/%F0%9F%93%9A_API_Docs-Swagger-0EA5E9?style=for-the-badge" alt="API Docs"/>`{=html}
`</a>`{=html}
`<a href="https://github.com/shubhamkardel-ai/RecruitRAG-AI">`{=html}
`<img src="https://img.shields.io/badge/%F0%9F%92%BB_Source-GitHub-111827?style=for-the-badge&logo=github" alt="GitHub"/>`{=html}
`</a>`{=html}

`<br/>`{=html}

`<img src="https://readme-typing-svg.demolab.com?font=Orbitron&weight=600&size=22&pause=900&color=00F7FF&center=true&vCenter=true&width=850&lines=Resume+Intelligence+%7C+RAG+%7C+Job+Matching;Candidate+Evaluation+%7C+Interview+Intelligence;FastAPI+%2B+Streamlit+%2B+Qdrant+%2B+Groq;From+Resume+Documents+to+Recruiter+Insights" alt="Typing animation"/>`{=html}
:::

------------------------------------------------------------------------

## 🧠 What is RecruitRAG-AI?

**RecruitRAG-AI** is an AI-powered recruitment intelligence platform
that turns candidate resumes into searchable, evaluatable, and
recruiter-friendly intelligence.

Instead of treating a resume as a static PDF, the platform builds a
complete pipeline:

**Resume → Document Intelligence → Candidate Evaluation → Vector
Retrieval → RAG → Job Matching → Interview Intelligence**

It combines deterministic recruitment logic with retrieval-augmented
generation so that AI responses remain grounded in the indexed candidate
information.

------------------------------------------------------------------------

## ⚡ Platform at a Glance

  -----------------------------------------------------------------------
  Capability                          What RecruitRAG-AI does
  ----------------------------------- -----------------------------------
  📄 Resume Intelligence              Accepts PDF, DOCX, and TXT resumes

  🧩 Document Ingestion               Extracts, cleans, and chunks resume
                                      content

  🎯 Candidate Evaluation             Calculates a deterministic
                                      100-point candidate score

  🔎 Semantic Retrieval               Searches resume chunks using vector
                                      similarity

  💬 Recruiter RAG                    Answers candidate questions using
                                      retrieved context

  🧠 Job Matching                     Compares indexed resume skills
                                      against a job description

  🎤 Interview Intelligence           Generates role-specific interview
                                      questions and evaluation points

  ☁️ Production Deployment            FastAPI on Render + Streamlit
                                      Cloud + Qdrant Cloud
  -----------------------------------------------------------------------

------------------------------------------------------------------------

## 🚀 Core Intelligence

### 01 · Candidate Evaluation

RecruitRAG-AI evaluates an indexed candidate using six deterministic
dimensions:

  Evaluation Dimension         Weight
  ------------------------- ---------
  Technical Skills                 20
  Project Experience               20
  Professional Experience          20
  Education                        15
  Certifications                   10
  Role Relevance                   15
  **Total**                   **100**

### Hiring Recommendation Logic

          Score Recommendation
  ------------- ------------------
    **80--100** 🟢 Strong Fit
     **65--79** 🔵 Potential Fit
     **50--64** 🟡 Needs Review
      **0--49** 🔴 Weak Fit

This layer is intentionally deterministic, making the primary candidate
score explainable and reproducible.

------------------------------------------------------------------------

### 02 · Retrieval-Augmented Generation

The RAG layer transforms resume content into searchable knowledge.

``` mermaid
flowchart LR
    A[Resume PDF DOCX TXT] --> B[Document Extraction]
    B --> C[Chunking]
    C --> D[FastEmbed<br/>BAAI/bge-small-en-v1.5]
    D --> E[384-D Embeddings]
    E --> F[(Qdrant<br/>Cosine Search)]
    F --> G[Top-K Relevant Context]
    G --> H[Groq LLM]
    H --> I[Grounded Recruiter Answer]
```

The generation prompt explicitly instructs the assistant to use
retrieved context, avoid inventing candidate information, and state when
the requested information is unavailable.

------------------------------------------------------------------------

### 03 · Job Description Matching

Recruiters can paste a target job description and compare it against the
indexed resume.

The matching engine:

-   extracts recognized skills from the job description
-   checks those skills against the indexed resume
-   calculates a percentage match
-   separates matching skills from missing skills

**Example production validation:**

> **83% Job Match**\
> Matching: Python, SQL, Pandas, Power BI, Machine Learning\
> Missing: Docker

------------------------------------------------------------------------

### 04 · AI Interview Intelligence

RecruitRAG-AI can generate a structured interview guide from the indexed
resume and target job description.

The guide contains:

1.  **Technical Interview Questions**
2.  **Project-Based Questions**
3.  **Experience-Based Questions**
4.  **Skill-Gap Questions**
5.  **Behavioral Questions**
6.  **Interviewer Evaluation Points**

This connects candidate evidence with the actual requirements of the
target role.

------------------------------------------------------------------------

## 🔄 End-to-End Recruitment Workflow

``` mermaid
flowchart TD
    A[Recruiter uploads resume] --> B[FastAPI Document API]
    B --> C[PDF / DOCX / TXT Extraction]
    C --> D[Text Chunking]
    D --> E[Candidate Evaluation]
    D --> F[FastEmbed]
    F --> G[(Qdrant Vector Database)]

    G --> H[RAG Recruiter Assistant]
    G --> I[Job Description Matching]
    G --> J[Interview Intelligence]

    I --> K[Match Score + Skill Gaps]
    J --> L[Interview Guide]
    H --> M[Grounded Candidate Answers]
    E --> N[Hiring Recommendation]
```

------------------------------------------------------------------------

## 🏗️ Production Architecture

``` mermaid
flowchart LR
    U[Recruiter] --> S[Streamlit Cloud<br/>Recruiter Dashboard]
    S --> R[Render<br/>FastAPI Backend]

    R --> Q[(Qdrant Cloud<br/>Vector Database)]
    R --> G[Groq<br/>LLM]

    R --> E[FastEmbed<br/>Embeddings]
    R --> D[Document Processing]

    Q --> R
    G --> R

    R --> S
    S --> U
```

### Deployment Stack

  Layer               Technology
  ------------------- ------------------------------------
  Frontend            Streamlit
  Backend             FastAPI
  Vector Database     Qdrant Cloud
  Local Vector DB     Qdrant Docker
  Embeddings          FastEmbed · BAAI/bge-small-en-v1.5
  LLM                 Groq
  Containerization    Docker
  Backend Hosting     Render
  Frontend Hosting    Streamlit Cloud
  API Documentation   FastAPI / Swagger

> **Deployment note:** the current Render backend uses the free tier, so
> the service may sleep after inactivity and require a cold start.

------------------------------------------------------------------------

## 🧩 Modular Project Architecture

``` text
RecruitRAG-AI/
│
├── app/
│   ├── api/
│   │   └── routes/
│   │       ├── documents.py
│   │       ├── matching.py
│   │       └── interview.py
│   │
│   ├── evaluation/
│   │   └── evaluator.py
│   │
│   ├── generation/
│   │   ├── llm.py
│   │   ├── prompts.py
│   │   └── response_generator.py
│   │
│   ├── ingestion/
│   │   └── pipeline.py
│   │
│   ├── interview/
│   │   ├── job_interviewer.py
│   │   └── interview_service.py
│   │
│   ├── matching/
│   │   ├── job_matcher.py
│   │   └── matching_service.py
│   │
│   ├── retrieval/
│   │   ├── embeddings.py
│   │   ├── retriever.py
│   │   └── vector_store.py
│   │
│   ├── services/
│   │   └── document_service.py
│   │
│   └── rag_pipeline.py
│
├── data/
│   └── uploads/
│
├── Dockerfile
├── docker-compose.yml
├── main.py
├── streamlit_app.py
├── requirements.txt
├── .env.example
├── .gitignore
└── README.md
```

------------------------------------------------------------------------

## 🔌 API Surface

  -----------------------------------------------------------------------
  Method                  Endpoint                Purpose
  ----------------------- ----------------------- -----------------------
  `POST`                  `/documents/upload`     Upload and index a
                                                  resume

  `POST`                  `/chat/ask`             Ask grounded questions
                                                  about indexed content

  `POST`                  `/matching/match`       Match resume against a
                                                  job description

  `POST`                  `/interview/generate`   Generate a
                                                  role-specific interview
                                                  guide

  `GET`                   `/docs`                 Interactive Swagger API
                                                  documentation
  -----------------------------------------------------------------------

### Example Request

``` json
{
  "job_description": "We are looking for an AI/ML Engineer with strong Python, SQL, Machine Learning, Pandas, NumPy, Scikit-learn and FastAPI skills."
}
```

------------------------------------------------------------------------

## 🛠️ Tech Stack

::: {align="center"}
`<img src="https://skillicons.dev/icons?i=python,fastapi,docker,git,github,streamlit&theme=dark" alt="Core technologies"/>`{=html}

`<br/>`{=html}`<br/>`{=html}

`<img src="https://img.shields.io/badge/Qdrant-Vector%20Database-DC2626?style=flat-square&logo=qdrant&logoColor=white"/>`{=html}
`<img src="https://img.shields.io/badge/FastEmbed-Embeddings-7C3AED?style=flat-square"/>`{=html}
`<img src="https://img.shields.io/badge/Groq-LLM-111827?style=flat-square"/>`{=html}
`<img src="https://img.shields.io/badge/PDF-DOCX-TXT-0EA5E9?style=flat-square"/>`{=html}
:::

------------------------------------------------------------------------

## 💻 Local Setup

### 1. Clone the repository

``` bash
git clone https://github.com/shubhamkardel-ai/RecruitRAG-AI.git
cd RecruitRAG-AI
```

### 2. Create a virtual environment

``` bash
python -m venv .venv
```

### 3. Activate it

**Windows PowerShell**

``` powershell
.venv\Scripts\Activate.ps1
```

### 4. Install dependencies

``` bash
pip install -r requirements.txt
```

### 5. Configure environment variables

Create `.env` from `.env.example`.

``` env
GROQ_API_KEY=your_groq_api_key
LLM_MODEL=openai/gpt-oss-120b

QDRANT_URL=
QDRANT_API_KEY=
```

For local development, Qdrant can run through Docker.

### 6. Start Qdrant

``` bash
docker compose up -d qdrant
```

### 7. Start the FastAPI backend

``` bash
uvicorn main:app --reload --port 8000
```

### 8. Start Streamlit

Open another terminal:

``` bash
streamlit run streamlit_app.py
```

The local application will normally be available at:

``` text
http://localhost:8501
```

Swagger:

``` text
http://localhost:8000/docs
```

------------------------------------------------------------------------

## 🐳 Docker

The project includes Docker configuration for running the application
stack.

``` bash
docker compose up --build
```

The local development architecture can run:

-   FastAPI backend
-   Streamlit frontend
-   Qdrant vector database

------------------------------------------------------------------------

## 🎯 How to Use

### Step 1 --- Upload a Resume

Upload a:

-   PDF
-   DOCX
-   TXT

RecruitRAG-AI extracts and chunks the content, evaluates the candidate,
generates embeddings, and indexes the chunks.

### Step 2 --- Review Candidate Intelligence

The dashboard presents:

-   candidate score
-   recommendation
-   evaluation breakdown
-   AI hiring insights
-   candidate summary

### Step 3 --- Ask Recruiter Questions

Use the RAG assistant to ask questions such as:

``` text
What are the candidate's technical skills?
```

``` text
What projects has the candidate worked on?
```

``` text
What Python experience is mentioned in the resume?
```

### Step 4 --- Compare With a Job

Paste a job description to receive:

-   match percentage
-   matching skills
-   missing skills

### Step 5 --- Generate an Interview Guide

Paste a target job description and generate a structured interview guide
based on the indexed candidate.

------------------------------------------------------------------------

## 📊 Production Validation

The deployed platform has been validated across its major recruitment
workflows.

  Test                         Result
  ---------------------------- -------------------------
  Resume upload                ✅ Passed
  PDF extraction               ✅ Passed
  Resume chunking              ✅ Passed
  Candidate evaluation         ✅ 98/100 · Strong Fit
  Vector indexing              ✅ 3 chunks / 3 vectors
  RAG question answering       ✅ Passed
  Job matching                 ✅ 83% validation
  Interview guide generation   ✅ Passed
  Streamlit → Render API       ✅ Passed
  Qdrant Cloud retrieval       ✅ Passed

### Example Evaluation

**Candidate Score:** `98 / 100`\
**Recommendation:** `Strong Fit`

### Example Match

**Job Match:** `83%`

**Matching skills:** Python · SQL · Pandas · Power BI · Machine Learning

**Missing skill:** Docker

------------------------------------------------------------------------

## 🔐 Security

RecruitRAG-AI follows a basic production-oriented secret-management
approach:

-   API keys are stored in environment variables.
-   `.env` is excluded from Git.
-   `.env.example` contains placeholders only.
-   Production secrets belong to the backend deployment environment.
-   Secrets should never be committed to GitHub.
-   If a real credential is ever exposed, it should be revoked and
    rotated immediately.

------------------------------------------------------------------------

## 🧠 Engineering Principles

RecruitRAG-AI is designed around several practical engineering
principles:

**Grounded AI**\
LLM responses are generated from retrieved candidate context rather than
unrestricted model knowledge.

**Deterministic Evaluation**\
The primary candidate score is rule-based and reproducible.

**Modular Architecture**\
Ingestion, evaluation, retrieval, generation, matching, and interview
logic are separated into dedicated services.

**API-First Backend**\
Recruitment intelligence is exposed through FastAPI endpoints and can be
consumed by the Streamlit frontend.

**Production-Aware Design**\
The project separates local development infrastructure from cloud
deployment infrastructure.

------------------------------------------------------------------------

## 🔮 Future Evolution

These are planned directions, not current features:

-   Multi-resume candidate comparison
-   Recruiter ranking and shortlist workflows
-   Advanced semantic job matching
-   Candidate skill-gap analytics
-   Interview answer evaluation
-   Recruiter conversation memory
-   Better document deduplication and versioning
-   Authentication and role-based access
-   Observability and production monitoring
-   Evaluation datasets and automated RAG quality benchmarks

------------------------------------------------------------------------

## 🌐 Live Project

::: {align="center"}
### 🚀 RecruitRAG-AI

`<a href="https://recruitrag-ai-szgzxyf5eum4c9lg4xtvxq.streamlit.app/">`{=html}
`<img src="https://img.shields.io/badge/%F0%9F%96%A5%EF%B8%8F_Open_Live_App-00F7FF?style=for-the-badge&logo=streamlit&logoColor=111827" alt="Open Live App"/>`{=html}
`</a>`{=html}

`<a href="https://recruitrag-ai-api.onrender.com/docs">`{=html}
`<img src="https://img.shields.io/badge/%F0%9F%94%8C_Open_API-0EA5E9?style=for-the-badge&logo=fastapi&logoColor=white" alt="Open API"/>`{=html}
`</a>`{=html}

`<a href="https://github.com/shubhamkardel-ai/RecruitRAG-AI">`{=html}
`<img src="https://img.shields.io/badge/%F0%9F%92%BB_View_Source-111827?style=for-the-badge&logo=github&logoColor=white" alt="View Source"/>`{=html}
`</a>`{=html}
:::

------------------------------------------------------------------------

## 👨‍💻 Author

::: {align="center"}
### **Shubham Kardel**

**Aspiring AI/ML Engineer · Python Developer · GenAI Builder**

`<a href="https://github.com/shubhamkardel-ai">`{=html}
`<img src="https://img.shields.io/badge/GitHub-shubhamkardel--ai-111827?style=for-the-badge&logo=github"/>`{=html}
`</a>`{=html}

`<a href="https://www.linkedin.com/in/shubham-kardel-303356312/">`{=html}
`<img src="https://img.shields.io/badge/LinkedIn-Shubham%20Kardel-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white"/>`{=html}
`</a>`{=html}
:::

------------------------------------------------------------------------

::: {align="center"}
`<img src="https://readme-typing-svg.demolab.com?font=Orbitron&weight=500&size=18&pause=1200&color=00F7FF&center=true&vCenter=true&width=750&lines=Build+with+Purpose.;Retrieve+with+Context.;Generate+with+Grounding.;Engineer+for+Reality." alt="Closing animation"/>`{=html}

`<br/>`{=html}

`<img src="https://capsule-render.vercel.app/api?type=waving&color=0:00F7FF,35:007C91,70:061A3A,100:020617&height=130&section=footer&animation=fadeIn" width="100%"/>`{=html}
:::
