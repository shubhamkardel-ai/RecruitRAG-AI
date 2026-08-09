from pathlib import Path
import shutil

from fastapi import APIRouter, UploadFile, File, HTTPException
from qdrant_client import QdrantClient

from app.services.document_service import DocumentService


UPLOAD_DIR = Path("data/uploads")
UPLOAD_DIR.mkdir(parents=True, exist_ok=True)


def create_document_router(
    client: QdrantClient,
) -> APIRouter:

    router = APIRouter(
        prefix="/documents",
        tags=["Documents"],
    )

    document_service = DocumentService(
        client=client
    )

    @router.post("/upload")
    async def upload_document(
        file: UploadFile = File(...),
    ):
        """
        Upload and index a document.

        Supported formats:
        - PDF
        - DOCX
        - TXT
        """

        if not file.filename:
            raise HTTPException(
                status_code=400,
                detail="No filename provided.",
            )

        extension = Path(
            file.filename
        ).suffix.lower()

        allowed_extensions = {
            ".pdf",
            ".docx",
            ".txt",
        }

        if extension not in allowed_extensions:
            raise HTTPException(
                status_code=400,
                detail=(
                    "Unsupported file type. "
                    "Use PDF, DOCX, or TXT."
                ),
            )

        file_path = UPLOAD_DIR / file.filename

        try:
            with file_path.open("wb") as buffer:
                shutil.copyfileobj(
                    file.file,
                    buffer,
                )

            result = document_service.index_document(
                str(file_path)
            )

            return result

        except Exception as exc:
            raise HTTPException(
                status_code=500,
                detail=str(exc),
            )

        finally:
            await file.close()

    return router