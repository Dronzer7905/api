from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.db.session import SessionLocal
from app.crud.employee import create_employee, get_employee_by_age, get_employee, delete, update_employee
from fastapi import HTTPException

router = APIRouter(prefix="/employee", tags=["Employee"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/")
def create_employee_endpoint(name: str, email: str, age: int, db: Session = Depends(get_db)):
    return create_employee(db, name, email, age)

@router.get("/")
def get_employees_endpoint(db: Session = Depends(get_db)):
    return get_employee(db)

@router.get("/by-age")
def get_employees_by_age_endpoint(age: int, db: Session = Depends(get_db)):
    return get_employee_by_age(db, age)

@router.put("/{id}")
def update_employee_endpoint(id: int, name: str, email: str, age: int, db: Session = Depends(get_db)):
    return update_employee(db, id, name, email, age)

@router.delete("/{id}")
def delete_employee_endpoint(id: int, db: Session = Depends(get_db)):
    return delete(db, id)