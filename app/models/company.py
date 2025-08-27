
from sqlalchemy import Column, Integer, String
from app.db.session import Base

class Company(Base):
    __tablename__ = "employees"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), index=True)
    email = Column(String(255))
    age = Column(Integer)

