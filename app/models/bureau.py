from sqlalchemy import Column, Float, Integer, String

from app.db.database import Base


class Bureau(Base):
    __tablename__ = "bureau"

    SK_ID_BUREAU = Column(Integer, primary_key=True, index=True)
    SK_ID_CURR = Column(Integer, index=True)
    CREDIT_ACTIVE = Column(String)
    CREDIT_CURRENCY = Column(String)
    DAYS_CREDIT = Column(Integer)
    CREDIT_DAY_OVERDUE = Column(Integer)
    DAYS_CREDIT_ENDDATE = Column(Float)
    DAYS_ENDDATE_FACT = Column(Float)
    AMT_CREDIT_MAX_OVERDUE = Column(Float)
    CNT_CREDIT_PROLONG = Column(Integer)
    AMT_CREDIT_SUM = Column(Float)
    AMT_CREDIT_SUM_DEBT = Column(Float)
    AMT_CREDIT_SUM_LIMIT = Column(Float)
    AMT_CREDIT_SUM_OVERDUE = Column(Float)
    CREDIT_TYPE = Column(String)
    DAYS_CREDIT_UPDATE = Column(Integer)
    AMT_ANNUITY = Column(Float)
