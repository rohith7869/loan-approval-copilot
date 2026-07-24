from sqlalchemy import Column, Float, Integer, String

from app.db.database import Base


class CreditCardBalance(Base):
    __tablename__ = "credit_card_balance"

    id = Column(Integer, primary_key=True, autoincrement=True)
    SK_ID_PREV = Column(Integer, index=True)
    SK_ID_CURR = Column(Integer, index=True)
    MONTHS_BALANCE = Column(Integer)
    AMT_BALANCE = Column(Float)
    AMT_CREDIT_LIMIT_ACTUAL = Column(Integer)
    AMT_DRAWINGS_ATM_CURRENT = Column(Float)
    AMT_DRAWINGS_CURRENT = Column(Float)
    AMT_DRAWINGS_OTHER_CURRENT = Column(Float)
    AMT_DRAWINGS_POS_CURRENT = Column(Float)
    AMT_INST_MIN_REGULARITY = Column(Float)
    AMT_PAYMENT_CURRENT = Column(Float)
    AMT_PAYMENT_TOTAL_CURRENT = Column(Float)
    AMT_RECEIVABLE_PRINCIPAL = Column(Float)
    AMT_RECIVABLE = Column(Float)
    AMT_TOTAL_RECEIVABLE = Column(Float)
    CNT_DRAWINGS_ATM_CURRENT = Column(Float)
    CNT_DRAWINGS_CURRENT = Column(Integer)
    CNT_DRAWINGS_OTHER_CURRENT = Column(Float)
    CNT_DRAWINGS_POS_CURRENT = Column(Float)
    CNT_INSTALMENT_MATURE_CUM = Column(Float)
    NAME_CONTRACT_STATUS = Column(String)
    SK_DPD = Column(Integer)
    SK_DPD_DEF = Column(Integer)
