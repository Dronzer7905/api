from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.db.session import SessionLocal
from app.services.student import create_student, get_student_by_age, get_student, delete, update_student
from fastapi import HTTPException
from app.services.database import get_db

router = APIRouter(prefix="/students", tags=["Student"])


@router.post("/")
def create_student(name: str, email: str, age: int,standard:int, db: Session = Depends(get_db)):
    return create_student(db, name, email, age,standard)

@router.get("/")
def get_students(db: Session = Depends(get_db)):
    return get_student(db)

@router.get("/by-age")
def get_students_by_age(age: int, db: Session = Depends(get_db)):
    return get_student_by_age(db, age)

@router.put("/{id}")
def update_student(id: int, name: str, email: str, age: int, db: Session = Depends(get_db)):
    return update_student(db, id, name, email, age)

@router.delete("/{id}")
def delete_student(id: int, db: Session = Depends(get_db)):
    return delete(db, id)