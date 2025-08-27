from sqlalchemy.orm import Session
from app.models.students_form import Student as stu

def create_student(db: Session, name: str, email: str, age: int,standard:int):
    student = stu(name=name, email=email, age=age,standard=standard)
    db.add(student)
    db.commit()
    db.refresh(student)
    return student

def get_student_by_age(db: Session, age: int):
    students = db.query(stu).filter(stu.age == age).all()
    return students

def get_student(db: Session):
    students = db.query(stu).all()
    return students

def delete(db: Session, id: int):
    obj = db.query(stu).filter(stu.id == id).first()
    db.delete(obj)
    db.commit()
    return obj

def update_student(db: Session, id: int, name: str, email: str, age: int):
    obj = db.query(stu).filter(stu.id == id).first()
    obj.name = name
    obj.email = email
    obj.age = age
    db.commit()
    db.refresh(obj)
    return obj
