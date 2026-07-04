from fastapi import APIRouter

router = APIRouter()


@router.get("/")
def predict_stub():
    """Placeholder – will accept applicant data and return loan decision."""
    return {"message": "Prediction endpoint coming soon"}