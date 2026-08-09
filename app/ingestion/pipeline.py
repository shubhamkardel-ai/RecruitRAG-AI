from pathlib import Path

from app.ingestion.loader import load_document
from app.ingestion.parser import clean_text
from app.ingestion.chunker import DocumentChunk, chunk_text


def ingest_document(
    file_path: str,
    chunk_size: int = 1000,
    chunk_overlap: int = 150,
) -> list[DocumentChunk]:
    """
    Complete document ingestion pipeline.

    Flow:
        Document
        → Load
        → Clean
        → Chunk
    """

    path = Path(file_path)

    if not path.exists():
        raise FileNotFoundError(
            f"Document not found: {file_path}"
        )

    # 1. Extract raw text
    raw_text = load_document(file_path)

    if not raw_text:
        raise ValueError(
            f"No text could be extracted from: {file_path}"
        )

    # 2. Clean and normalize text
    cleaned_text = clean_text(raw_text)

    if not cleaned_text:
        raise ValueError(
            f"No usable text remains after cleaning: {file_path}"
        )

    # 3. Split into chunks
    chunks = chunk_text(
        cleaned_text,
        chunk_size=chunk_size,
        chunk_overlap=chunk_overlap,
    )

    if not chunks:
        raise ValueError(
            f"Document produced no chunks: {file_path}"
        )

    return chunks