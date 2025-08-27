from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.db.session import SessionLocal
from app.services.staffMembers import create_staffmembers, get_staffmembers_by_age, get_staffmembers, delete, update_staffmembers
from fastapi import HTTPException
from app.services.database import get_db

router = APIRouter(prefix="/staffmembers", tags=["StaffMembers"])



# Create staff member
@router.post("/")
def create_staffmember(name: str, email: str, age: int, db: Session = Depends(get_db)):
    return create_staffmembers(db, name, email, age)

# Get all staff members
@router.get("/")
def get_staffmembers(db: Session = Depends(get_db)):
    return get_staffmembers(db)

# Get staff members by age
@router.get("/by-age")
def get_staffmembers_by_age(age: int, db: Session = Depends(get_db)):
    return get_staffmembers_by_age(db, age)

# Update staff member
@router.put("/{id}")
def update_staffmember(id: int, name: str, email: str, age: int, db: Session = Depends(get_db)):
    return update_staffmembers(db, id, name, email, age)

# Delete staff member
@router.delete("/{id}")
def delete_staffmember(id: int, db: Session = Depends(get_db)):
    return delete(db, id)
