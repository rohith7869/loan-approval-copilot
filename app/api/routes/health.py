from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter()


class HealthResponse(BaseModel):
    status: str
    version: str


@router.get("/health", response_model=HealthResponse)
def health_check():
    """Returns 200 OK when the service is running."""
    return HealthResponse(status="healthy", version="0.1.0")