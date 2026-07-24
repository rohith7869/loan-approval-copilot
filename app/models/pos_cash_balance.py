from sqlalchemy import Column, Float, Integer, String

from app.db.database import Base


class POSCashBalance(Base):
    __tablename__ = "pos_cash_balance"

    id = Column(Integer, primary_key=True, autoincrement=True)
    SK_ID_PREV = Column(Integer, index=True)
    SK_ID_CURR = Column(Integer, index=True)
    MONTHS_BALANCE = Column(Integer)
    CNT_INSTALMENT = Column(Float)
    CNT_INSTALMENT_FUTURE = Column(Float)
    NAME_CONTRACT_STATUS = Column(String)
    SK_DPD = Column(Integer)
    SK_DPD_DEF = Column(Integer)
