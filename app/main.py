from fastapi import FastAPI

from app.api.routes import health, predict, rag

app = FastAPI(
    title="Loan Approval & Borrower Copilot",
    description="Traditional ML loan prediction + RAG-powered borrower Q&A",
    version="0.1.0",
)

# --- Routers ---
app.include_router(health.router, tags=["Health"])
app.include_router(predict.router, prefix="/predict", tags=["Loan Prediction"])
app.include_router(rag.router, prefix="/rag", tags=["Borrower Copilot"])


def start():
    """Entry point for poetry run start"""
    import uvicorn

    uvicorn.run("app.main:app", host="0.0.0.0", port=8000, reload=True)
