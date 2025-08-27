from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.db.session import SessionLocal
from app.crud.staffMembers import create_staffmembers, get_staffmembers_by_age, get_staffmembers, delete, update_staffmembers
from fastapi import HTTPException

router = APIRouter(prefix="/staffmembers", tags=["StaffMembers"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Create staff member
@router.post("/")
def create_staffmember_endpoint(name: str, email: str, age: int, db: Session = Depends(get_db)):
    return create_staffmembers(db, name, email, age)

# Get all staff members
@router.get("/")
def get_staffmembers_endpoint(db: Session = Depends(get_db)):
    return get_staffmembers(db)

# Get staff members by age
@router.get("/by-age")
def get_staffmembers_by_age_endpoint(age: int, db: Session = Depends(get_db)):
    return get_staffmembers_by_age(db, age)

# Update staff member
@router.put("/{id}")
def update_staffmember_endpoint(id: int, name: str, email: str, age: int, db: Session = Depends(get_db)):
    return update_staffmembers(db, id, name, email, age)

# Delete staff member
@router.delete("/{id}")
def delete_staffmember_endpoint(id: int, db: Session = Depends(get_db)):
    return delete(db, id)
