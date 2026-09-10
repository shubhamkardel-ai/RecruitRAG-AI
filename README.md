::: {align="center"}
<img src="https://capsule-render.vercel.app/api?type=waving&color=0:020617,30:062A45,60:007C91,100:00F7FF&height=220&section=header&text=RecruitRAG-AI&fontSize=58&fontColor=FFFFFF&fontAlignY=38&desc=AI-Powered%20Recruitment%20Intelligence&descAlignY=62&descSize=20&animation=fadeIn" width="100%"/>{=html}

<br>{=html}

<a href="https://recruitrag-ai-szgzxyf5eum4c9lg4xtvxq.streamlit.app/">{=html}
<img src="https://readme-typing-svg.demolab.com?font=Orbitron&weight=700&size=22&duration=2800&pause=700&color=00F7FF&center=true&vCenter=true&width=850&lines=Resume+Understanding+%E2%9A%A1+Candidate+Evaluation;RAG-Powered+Recruiter+Intelligence+%F0%9F%A7%A0;Job+Matching+%F0%9F%8E%AF+%7C+Skill-Gap+Detection+%F0%9F%94%8E;AI+Interview+Intelligence+%F0%9F%A4%96;From+Resume+Data+to+Recruiter+Decisions+%F0%9F%9A%80" alt="Typing animation"/>{=html}
</a>{=html}

<br>{=html}<br>{=html}

<a href="https://recruitrag-ai-szgzxyf5eum4c9lg4xtvxq.streamlit.app/">{=html}
<img src="https://img.shields.io/badge/%F0%9F%9A%80_LIVE_DEMO-00F7FF?style=for-the-badge&logo=streamlit&logoColor=black" />{=html}
</a>{=html}
<a href="https://github.com/shubhamkardel-ai/RecruitRAG-AI">{=html}
<img src="https://img.shields.io/badge/%E2%98%81%EF%B8%8F_GITHUB-181717?style=for-the-badge&logo=github" />{=html}
</a>{=html}
<a href="https://recruitrag-ai-api.onrender.com/docs">{=html}
<img src="https://img.shields.io/badge/%F0%9F%93%9A_API_DOCS-009688?style=for-the-badge&logo=fastapi&logoColor=white" />{=html}
</a>{=html}

<br>{=html}<br>{=html}

<img src="https://img.shields.io/badge/AI%2FML-RAG-00F7FF?style=flat-square"/>{=html}
<img src="https://img.shields.io/badge/LLM-Groq-FF6B6B?style=flat-square"/>{=html}
<img src="https://img.shields.io/badge/Vector_DB-Qdrant-8B5CF6?style=flat-square"/>{=html}
<img src="https://img.shields.io/badge/Backend-FastAPI-009688?style=flat-square"/>{=html}
<img src="https://img.shields.io/badge/Frontend-Streamlit-FF4B4B?style=flat-square"/>{=html}
<img src="https://img.shields.io/badge/Deployment-Render%20%7C%20Streamlit%20Cloud-00A67E?style=flat-square"/>{=html}
:::

::: {align="center"}

🧬 RESUME → RETRIEVE → EVALUATE → MATCH → INTERVIEW → DECIDE

:::

🧠 What is RecruitRAG-AI?

RecruitRAG-AI is a production-deployed AI recruitment intelligence
platform that turns unstructured candidate resumes into an interactive,
evidence-grounded recruitment workflow.

Instead of treating a resume as a static PDF, the system transforms
candidate information into a searchable knowledge layer and combines
Retrieval-Augmented Generation (RAG) with deterministic recruitment
logic.

                         
                                CANDIDATE RESUME      
                                 PDF / DOCX / TXT     
                         
                                        
                                        ▼
                         
                              DOCUMENT INTELLIGENCE    
                            Extract → Chunk → Embed    
                         
                                        
                                        ▼
                         
                                QDRANT VECTOR DB       
                              Semantic Candidate KB    
                         
                                        
                    
                                                          
                    ▼                   ▼                   ▼
                     
                RAG CHAT       JOB MATCHING      INTERVIEW  
                                                INTELLIGENCE
                     
                                                         
                    
                                       ▼
                            
                                 GROQ LLM       
                             Context-Grounded   
                             Response Generation
                            
                                      
                                      ▼
                         
                             RECRUITER DECISION   
                          Score • Match • Skills  
                          Questions • Insights    
                         

⚡ The Recruiter Intelligence Layer

<table>

<tr>

<td width="50%" valign="top">

📄 Resume Intelligence

Upload PDF, DOCX or TXT resumes and convert them into structured,
searchable candidate knowledge.

</td>

<td width="50%" valign="top">

🎯 Candidate Evaluation

Score candidates across technical skills, projects, experience,
education, certifications and role relevance.

</td>

</tr>

<tr>

<td width="50%" valign="top">

🔎 Job Matching

Compare an indexed candidate against a target role and identify
matching + missing skills.

</td>

<td width="50%" valign="top">

🎤 Interview Intelligence

Generate role-specific technical, project, experience, behavioral and
skill-gap questions.

</td>

</tr>

<tr>

<td width="50%" valign="top">

🧠 RAG Recruiter Assistant

Ask natural-language questions and retrieve candidate-grounded answers
from the indexed resume.

</td>

<td width="50%" valign="top">

☁️ Production Deployment

FastAPI + Streamlit + Qdrant Cloud + Groq deployed as a real working
application.

</td>

</tr>

</table>

🎯 Candidate Evaluation Engine

RecruitRAG-AI combines deterministic scoring with AI-assisted insights.

::: {align="center"}
Evaluation Dimension            Weight

🧠 Technical Skills             20
🚀 Project Experience           20
💼 Professional Experience      20
🎓 Education                    15
📜 Certifications               10
🎯 Role Relevance               15
TOTAL                      100
:::

Recommendation Logic

100  ████████████████████████████████████████  Strong Fit
 80 
 65  ██████████████████████████                Potential Fit
 50  ████████████████████                      Needs Review
  0  █████                                     Weak Fit

Production Validation


          CANDIDATE EVALUATION              

                                            
              98 / 100                      
                                            
             STRONG FIT                     
                                            
  Technical Skills ............... 20/20    
  Project Experience ............ 20/20    
  Professional Experience ....... 20/20    
  Education ..................... 15/15    
  Certifications ................ 10/10    
  Role Relevance ................ 13/15    
                                            

🔥 Job Description Intelligence

A recruiter can paste a target job description and instantly compare it
with the indexed candidate.

                    TARGET JOB
                        
                        ▼
              
               Requirement Scan 
              
                       
             
             ▼                   ▼
       MATCHING SKILLS      MISSING SKILLS
                                
             
                       ▼
                 MATCH SCORE

Example Production Result

🎯 JOB MATCH SCORE

                    86%
              █████████████████░░░

✅ MATCHING
Python
SQL
Pandas
NumPy
Scikit-learn
Machine Learning

⚠️ MISSING
FastAPI

The system therefore does not simply say "good candidate" --- it
exposes the skill alignment and skill gap.

🤖 AI Interview Intelligence

Once a job description is supplied, RecruitRAG-AI generates a structured
interview guide around the candidate and role.

                    JOB DESCRIPTION
                           +
                     CANDIDATE RESUME
                           
                           ▼
                 
                  Interview Analyzer 
                 
                           
       
       ▼                   ▼                   ▼
  TECHNICAL             PROJECT             EXPERIENCE
  QUESTIONS             QUESTIONS            QUESTIONS
                                             
       
                           ▼
                    SKILL-GAP QUESTIONS
                           
                           ▼
                    BEHAVIORAL QUESTIONS
                           
                           ▼
                 EVALUATION POINTS

Generated Interview Guide

🧠 Technical Interview Questions

🚀 Project-Based Questions

💼 Experience-Based Questions

⚠️ Skill-Gap Questions

🗣️ Behavioral Questions

📊 Interviewer Evaluation Points

💬 Recruiter Intelligence

The recruiter can interact with the candidate knowledge base naturally.


 Recruiter Question                           
                                              
 "What are the candidate's strongest         
  technical skills?"                          

                       
                       ▼
                Semantic Retrieval
                       
                       ▼
                 Resume Context
                       
                       ▼
                  Groq LLM
                       
                       ▼

 Evidence-Grounded Candidate Answer           

Example Questions

→ What are the candidate's strongest technical skills?
→ What AI/ML projects has the candidate built?
→ Does the candidate have Python experience?
→ What experience does the candidate have?
→ What skills are missing for this role?

🧠 RAG Engine

The RAG layer is the intelligence backbone of RecruitRAG-AI.

Retrieval Flow

User Query
    
    ▼
Query Embedding
    
    ▼
Qdrant Semantic Search
    
    ▼
Top-K Relevant Resume Chunks
    
    ▼
Context Construction
    
    ▼
Groq LLM
    
    ▼
Grounded Response

Embedding Model

BAAI/bge-small-en-v1.5
        
        ▼
384-dimensional vectors
        
        ▼
Qdrant COSINE similarity

The system is explicitly instructed to avoid inventing candidate
information outside the retrieved context.

🏗️ Production Architecture

::: {align="center"}

                         INTERNET
                            
             
                                          
             ▼                             ▼
      STREAMLIT CLOUD                    RENDER
        FRONTEND                       FASTAPI API
                                          
                               
                                                   
                               ▼          ▼          ▼
                            RAG API   Matching   Interview
                               
                               ▼
                          QDRANT CLOUD
                               
                               ▼
                          GROQ LLM
             
             ► RECRUITER

:::

Deployment Stack

Layer                  Technology

🎨 Frontend            Streamlit Cloud
⚡ API                 FastAPI
☁️ Backend Hosting R   ender
🧠 LLM                 Groq
🔎 Vector Database     Qdrant Cloud
🧬 Embeddings          FastEmbed / BGE-small-en-v1.5
🐳 Containerization    Docker
🔐 Configuration       Environment Variables

🛠️ Technology Matrix

::: {align="center"}
<img src="https://skillicons.dev/icons?i=python,fastapi,docker,git,github&theme=dark" />{=html}

<br>{=html}<br>{=html}

<img src="https://skillicons.dev/icons?i=html,css&theme=dark" />{=html}
:::

AI / Data Layer

Python
 FastEmbed
 Qdrant
 Groq
 Pydantic
 RAG Pipeline

Application Layer

Streamlit
        ↓
FastAPI
        ↓
Service Layer
        ↓
Retrieval / Evaluation / Matching / Interview

📁 Architecture at a Glance

RecruitRAG-AI/

 app/
    api/
       routes/
           documents.py
           matching.py
           interview.py
   
    ingestion/
       pipeline.py
   
    retrieval/
       embeddings.py
       retriever.py
       vector_store.py
   
    generation/
       llm.py
       prompts.py
       response_generator.py
   
    evaluation/
       evaluator.py
   
    matching/
       job_matcher.py
       matching_service.py
   
    interview/
       job_interviewer.py
       interview_service.py
   
    rag_pipeline.py

 data/
    uploads/

 main.py
 streamlit_app.py
 Dockerfile
 docker-compose.yml
 requirements.txt
 .env.example
 .gitignore
 README.md

🔌 API Surface

Method  Endpoint                Purpose

POST  /documents/upload     Upload + index candidate resume
POST  /chat/ask             Ask recruiter questions
POST  /matching/match       Match resume against job description
POST  /interview/generate   Generate interview intelligence

Interactive API

<a href="https://recruitrag-ai-api.onrender.com/docs">{=html}
<img src="https://img.shields.io/badge/OPEN_FASTAPI_SWAGGER-00F7FF?style=for-the-badge&logo=fastapi&logoColor=black"/>{=html}
</a>{=html}

🧪 Production Verification

RecruitRAG-AI has been validated through the deployed application.


              PRODUCTION CHECK              

                                            
  🟢 API Connected                          
  🔵 RAG Engine Active                      
  🔵 AI Assistant Active                    
                                            
  📄 Resume Indexing             PASSED     
  🎯 Candidate Evaluation        PASSED     
  🔎 Job Matching                PASSED     
  🤖 Interview Intelligence      PASSED     
  💬 Recruiter Intelligence      PASSED     
                                            
  🚀 DEPLOYMENT STATUS: LIVE                
                                            

Verified Example

Candidate Score       → 98/100
Recommendation        → Strong Fit
Job Match             → 86%
Missing Skill         → FastAPI
Interview Guide       → Generated
RAG Q&A               → Working

🚀 Quick Start

1. Clone

git clone https://github.com/shubhamkardel-ai/RecruitRAG-AI.git
cd RecruitRAG-AI

2. Create environment

python -m venv .venv

Windows

.venv\Scripts\activate

3. Install

pip install -r requirements.txt

4. Configure .env

GROQ_API_KEY=your_groq_api_key
LLM_MODEL=openai/gpt-oss-120b
QDRANT_URL=your_qdrant_url
QDRANT_API_KEY=your_qdrant_api_key

⚠️ Never commit .env or production credentials.

5. Start FastAPI

uvicorn main:app --reload --port 8000

6. Start Streamlit

streamlit run streamlit_app.py

🐳 Docker

docker compose up --build

Development architecture:

Streamlit
    
    ▼
FastAPI
    
    ▼
Qdrant
    
    ▼
Groq

🔐 Security

RecruitRAG-AI keeps credentials outside the source code.

.env
   ↓
Environment Variables
   ↓
Backend Services

The repository uses .env.example only for documenting required
configuration.

Security rule:

❌ API keys in source code
❌ API keys in README
❌ API keys in Git history

✅ Environment variables
✅ Secret management
✅ Credential rotation

🧩 Engineering Highlights

This project demonstrates hands-on implementation of:

AI Engineering
 Retrieval-Augmented Generation
 Semantic Search
 Embeddings
 LLM Integration
 Prompt Engineering

Backend Engineering
 FastAPI
 REST APIs
 Service Architecture
 Validation
 Error Handling

Data / ML Engineering
 Document Processing
 Text Chunking
 Vector Search
 Candidate Evaluation
 Skill Matching

Deployment Engineering
 Docker
 Render
 Streamlit Cloud
 Qdrant Cloud

🗺️ Future Evolution

                    CURRENT
                       
                       ▼
             
              RecruitRAG-AI    
              Single Candidate 
             
                      
          
          ▼           ▼           ▼
      Candidate    Recruiter    Interview
      Ranking      Analytics    Feedback
                                
          
                      ▼
             Multi-Candidate
                Intelligence
                      
                      ▼
              Recruitment AI
                 Platform

Planned Directions

👥 Multi-candidate comparison

🏆 Candidate ranking

📊 Recruiter analytics

🔐 Recruiter authentication

📝 Interview feedback tracking

📧 Recruitment workflow integration

📡 Production monitoring

⚡ Background document processing

🧪 Automated RAG evaluation

🌐 Explore the Project

::: {align="center"}
<a href="https://recruitrag-ai-szgzxyf5eum4c9lg4xtvxq.streamlit.app/">{=html}
<img src="https://img.shields.io/badge/%F0%9F%9A%80_TRY_LIVE_APPLICATION-00F7FF?style=for-the-badge&logo=streamlit&logoColor=black"/>{=html}
</a>{=html}

<br>{=html}<br>{=html}

<a href="https://github.com/shubhamkardel-ai/RecruitRAG-AI">{=html}
<img src="https://img.shields.io/github/stars/shubhamkardel-ai/RecruitRAG-AI?style=for-the-badge&logo=github&label=STARS"/>{=html}
</a>{=html}

<a href="https://github.com/shubhamkardel-ai/RecruitRAG-AI">{=html}
<img src="https://img.shields.io/github/forks/shubhamkardel-ai/RecruitRAG-AI?style=for-the-badge&logo=github&label=FORKS"/>{=html}
</a>{=html}
:::

👨‍💻 Built by

::: {align="center"}
<img src="https://readme-typing-svg.demolab.com?font=Orbitron&weight=700&size=24&duration=3000&pause=900&color=00F7FF&center=true&vCenter=true&width=650&lines=SHUBHAM+KARDEL;Aspiring+AI%2FML+Engineer;Building+%E2%80%A2+Learning+%E2%80%A2+Evolving" />{=html}

<br>{=html}

AI/ML • Python • Generative AI • RAG • NLP • AI Agents • MLOps

<br>{=html}<br>{=html}

<a href="https://github.com/shubhamkardel-ai">{=html}
<img src="https://img.shields.io/badge/GitHub-shubhamkardel--ai-181717?style=for-the-badge&logo=github"/>{=html}
</a>{=html}

<a href="https://linkedin.com/in/shubham-kardel-303356312/">{=html}
<img src="https://img.shields.io/badge/LinkedIn-Shubham_Kardel-0A66C2?style=for-the-badge&logo=linkedin"/>{=html}
</a>{=html}
:::

::: {align="center"}

⚡ FROM RESUME DATA → TO RECRUITER INTELLIGENCE

<br>{=html}

<img src="https://readme-typing-svg.demolab.com?font=Orbitron&weight=600&size=18&duration=2500&pause=800&color=00F7FF&center=true&vCenter=true&width=700&lines=Retrieve.;Evaluate.;Match.;Question.;Decide.;RecruitRAG-AI." />{=html}

<br>{=html}<br>{=html}

<img src="https://capsule-render.vercel.app/api?type=waving&color=0:00F7FF,35:007C91,70:062A45,100:020617&height=140&section=footer&animation=fadeIn" width="100%"/>{=html}
:::
