
from sqlalchemy import Column, Integer, String
from app.db.session import Base
from pydantic import BaseModel, EmailStr

class Student(Base):
    __tablename__ = "students_data"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), index=True)
    email = Column(String(255), unique=True, index=True)
    age = Column(Integer)
    standard = Column(Integer)

