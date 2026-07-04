from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    # App
    APP_NAME: str = "Loan Approval & Borrower Copilot"
    DEBUG: bool = False

    # Database
    DATABASE_URL: str = "postgresql://user:password@localhost:5432/loan_db"

    # HuggingFace
    HF_TOKEN: str = ""

    # ML model path
    ML_MODEL_PATH: str = "app/ml/loan_model.joblib"

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"


settings = Settings()
