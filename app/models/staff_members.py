from sqlalchemy import Column, Integer, String
from app.db.session import Base

class StaffMembers(Base):
    __tablename__ = "staffMembers"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255))
    email = Column(String(255))
    age = Column(Integer)
