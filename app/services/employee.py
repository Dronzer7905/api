from sqlalchemy.orm import Session
from app.models.company import Company

def create_employee(db: Session, name: str, email: str, age: int):
    employee = Company(name=name, email=email, age=age)
    db.add(employee)
    db.commit()
    db.refresh(employee)
    return employee

def get_employee_by_age(db: Session, age: int):
    employees = db.query(Company).filter(Company.age == age).all()
    return employees

def get_employee(db: Session):
    employees = db.query(Company).all()
    return employees

def delete(db: Session, id: int):
    obj = db.query(Company).filter(Company.id == id).first()
    db.delete(obj)
    db.commit()
    return obj

def update_employee(db: Session, id: int, name: str, email: str, age: int):
    obj = db.query(Company).filter(Company.id == id).first()
    obj.name = name
    obj.email = email
    obj.age = age
    db.commit()
    db.refresh(obj)
    return obj
