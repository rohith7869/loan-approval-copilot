from sqlalchemy import Column, Float, Integer

from app.db.database import Base


class InstallmentsPayments(Base):
    __tablename__ = "installments_payments"

    id = Column(Integer, primary_key=True, autoincrement=True)
    SK_ID_PREV = Column(Integer, index=True)
    SK_ID_CURR = Column(Integer, index=True)
    NUM_INSTALMENT_VERSION = Column(Float)
    NUM_INSTALMENT_NUMBER = Column(Integer)
    DAYS_INSTALMENT = Column(Float)
    DAYS_ENTRY_PAYMENT = Column(Float)
    AMT_INSTALMENT = Column(Float)
    AMT_PAYMENT = Column(Float)
