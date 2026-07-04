from fastapi import APIRouter

router = APIRouter()


@router.get("/")
def rag_stub():
    """Placeholder – borrower Q&A endpoint coming soon."""
    return {"message": "RAG Q&A endpoint coming soon"}