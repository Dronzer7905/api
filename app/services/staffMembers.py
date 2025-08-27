from sqlalchemy.orm import Session
from app.models.staff_members import StaffMembers as school

def create_staffmembers(db: Session, name: str, email: str, age: int):
    staff_member = school(name=name, email=email, age=age)
    db.add(staff_member)
    db.commit()
    db.refresh(staff_member)
    return staff_member

def get_staffmembers_by_age(db: Session, age: int):
    staff = db.query(school).filter(school.age == age).all()
    return staff

def get_staffmembers(db: Session):
    staff = db.query(school).all()
    return staff

def delete(db: Session, id: int):
    obj = db.query(school).filter(school.id == id).first()
    db.delete(obj)
    db.commit()
    return obj

def update_staffmembers(db: Session, id: int, name: str, email: str, age: int):
    obj = db.query(school).filter(school.id == id).first()
    obj.name = name
    obj.email = email
    obj.age = age
    db.commit()
    db.refresh(obj)
    return obj
