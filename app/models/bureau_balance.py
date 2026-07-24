from sqlalchemy import Column, Integer, String

from app.db.database import Base


class BureauBalance(Base):
    __tablename__ = "bureau_balance"

    id = Column(Integer, primary_key=True, autoincrement=True)
    SK_ID_BUREAU = Column(Integer, index=True)
    MONTHS_BALANCE = Column(Integer)
    STATUS = Column(String)
