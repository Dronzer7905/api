from fastapi import FastAPI
from app.api.school import router as school_router
from app.api.employee import router as employee_router

# Import all models before table creation
from app.models.staff_members import StaffMembers
from app.models.company import Company
from app.db.session import engine, Base
from app.models.students_form import Student
from app.api.students import router as student_router
Base.metadata.create_all(engine)

app = FastAPI()
app.include_router(employee_router)
app.include_router(school_router)
app.include_router(student_router)

