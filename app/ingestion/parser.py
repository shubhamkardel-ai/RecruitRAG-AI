import re


def normalize_text(text: str) -> str:
    """
    Normalize extracted document text.

    - Removes excessive whitespace
    - Normalizes line breaks
    - Removes unwanted control characters
    """

    if not text:
        return ""

    # Normalize line endings
    text = text.replace("\r\n", "\n")
    text = text.replace("\r", "\n")

    # Remove control characters while preserving Unicode text.
    text = re.sub(r"[\x00-\x08\x0B\x0C\x0E-\x1F\x7F]", " ", text)

    # Remove excessive spaces
    text = re.sub(r"[ \t]+", " ", text)

    # Remove excessive blank lines
    text = re.sub(r"\n\s*\n+", "\n\n", text)

    return text.strip()


def clean_text(text: str) -> str:
    """
    Clean and normalize document text before chunking.
    """

    if not text:
        return ""

    text = normalize_text(text)

    # Fix spaces before punctuation
    text = re.sub(r"\s+([,.!?;:])", r"\1", text)

    # Normalize repeated punctuation
    text = re.sub(r"\.{3,}", "...", text)

    return text.strip()