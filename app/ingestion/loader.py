from pathlib import Path

from pypdf import PdfReader
from docx import Document


def load_pdf(file_path: str) -> str:
    """Extract text from a PDF file."""

    reader = PdfReader(file_path)

    pages = []

    for page in reader.pages:
        text = page.extract_text()

        if text:
            pages.append(text)

    return "\n\n".join(pages).strip()


def load_docx(file_path: str) -> str:
    """Extract text from a DOCX file."""

    document = Document(file_path)

    paragraphs = []

    for paragraph in document.paragraphs:
        text = paragraph.text.strip()

        if text:
            paragraphs.append(text)

    return "\n\n".join(paragraphs).strip()


def load_txt(file_path: str) -> str:
    """Extract text from a TXT file."""

    path = Path(file_path)

    return path.read_text(
        encoding="utf-8",
        errors="ignore"
    ).strip()


def load_document(file_path: str) -> str:
    """
    Load a supported document and return its extracted text.

    Supported formats:
    - PDF
    - DOCX
    - TXT
    """

    path = Path(file_path)

    if not path.exists():
        raise FileNotFoundError(
            f"Document not found: {file_path}"
        )

    extension = path.suffix.lower()

    if extension == ".pdf":
        return load_pdf(file_path)

    if extension == ".docx":
        return load_docx(file_path)

    if extension == ".txt":
        return load_txt(file_path)

    raise ValueError(
        f"Unsupported document format: {extension}"
    )