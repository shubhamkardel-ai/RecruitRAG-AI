def build_context(documents: list) -> str:
    """
    Convert retrieved documents into grounded LLM context.
    """

    context_parts = []

    for document in documents:
        context_parts.append(
            f"Source: {document.source}\n"
            f"Chunk ID: {document.chunk_id}\n"
            f"Relevance Score: {document.score:.4f}\n"
            f"Content:\n{document.text}"
        )

    return "\n\n---\n\n".join(context_parts)


def build_prompt(query: str, documents: list) -> str:
    """
    Build a grounded recruitment prompt from retrieved documents.
    """

    context = build_context(documents)

    return f"""
You are RecruitRAG-AI, an intelligent recruitment assistant.

Your job is to answer questions about candidates using ONLY
the information provided in the retrieved context.

Rules:
1. Never invent candidate information.
2. Use only information supported by the context.
3. If the answer cannot be found in the context, say:
   "The information is not available in the provided documents."
4. Give a professional and concise answer.
5. Mention relevant projects, skills, experience, or education
   only when supported by the context.
6. Do not mention embeddings, vector databases, or retrieval
   internals unless specifically asked.

RETRIEVED CONTEXT:
{context}

USER QUESTION:
{query}

ANSWER:
""".strip()