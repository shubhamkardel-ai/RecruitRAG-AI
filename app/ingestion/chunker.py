from dataclasses import dataclass


@dataclass
class DocumentChunk:
    """Represents a single chunk of a document."""

    content: str
    chunk_id: int
    start_index: int
    end_index: int


class TextChunker:
    """
    Splits cleaned document text into overlapping chunks.

    Overlap helps preserve context between neighboring chunks.
    """

    def __init__(
        self,
        chunk_size: int = 1000,
        chunk_overlap: int = 150,
    ):
        if chunk_size <= 0:
            raise ValueError("chunk_size must be greater than 0")

        if chunk_overlap < 0:
            raise ValueError("chunk_overlap cannot be negative")

        if chunk_overlap >= chunk_size:
            raise ValueError(
                "chunk_overlap must be smaller than chunk_size"
            )

        self.chunk_size = chunk_size
        self.chunk_overlap = chunk_overlap

    def split_text(self, text: str) -> list[DocumentChunk]:
        """
        Split text into overlapping chunks.
        """

        if not text or not text.strip():
            return []

        text = text.strip()

        chunks = []

        start = 0
        chunk_id = 0
        text_length = len(text)

        while start < text_length:
            end = min(
                start + self.chunk_size,
                text_length,
            )

            chunk_content = text[start:end].strip()

            if chunk_content:
                chunks.append(
                    DocumentChunk(
                        content=chunk_content,
                        chunk_id=chunk_id,
                        start_index=start,
                        end_index=end,
                    )
                )

                chunk_id += 1

            if end >= text_length:
                break

            start = end - self.chunk_overlap

        return chunks


def chunk_text(
    text: str,
    chunk_size: int = 1000,
    chunk_overlap: int = 150,
) -> list[DocumentChunk]:
    """
    Convenience function for splitting text into chunks.
    """

    chunker = TextChunker(
        chunk_size=chunk_size,
        chunk_overlap=chunk_overlap,
    )

    return chunker.split_text(text)