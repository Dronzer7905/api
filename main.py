from fastapi import FastAPI, Depends, APIRouter
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker, declarative_base, Session

# --- 1. Database Setup ---

# MySQL connection string (update user, password, host, db as needed)
mysql_url = "mysql+mysqlconnector://root:Ansh7905$@localhost:3306/fastapi_db"

# The engine manages the database connection (no connect_args needed for MySQL)
engine = create_engine(mysql_url, echo=True)

# The base class for our models
Base = declarative_base()

# A factory to create new database sessions
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


# --- 2. Database Model ---
# This class represents the 'heroes' table
class company(Base):
    __tablename__ = "employees"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), index=True)
    secret_name = Column(String(255))
    age = Column(Integer)


# --- 3. Database Functions ---
# Function to create tables
def create_db_and_tables():
    Base.metadata.create_all(engine)

# Dependency function to provide a database session for each request
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()



# --- 4. FastAPI Application ---
# Create the FastAPI app instance
app = FastAPI()

# This event runs once at startup to create the database tables
from contextlib import asynccontextmanager

@asynccontextmanager
async def lifespan(app: FastAPI):
    create_db_and_tables()
    yield

app = FastAPI(lifespan=lifespan)

# --- 6. API Endpoint to Fetch Data by Age ---
@app.get("/employees/by-age")
def get_employee_by_age(age: int, db: Session = Depends(get_db)):
    """
    Fetches all heroes with the specified age.
    """
    employees = db.query(company).filter(company.age == age).all()
    return employees


# --- 5. API Endpoint to Add Data ---
@app.post("/employees/")
def create_employee(name: str, secret_name: str, age: int, db: Session = Depends(get_db)):
    """
    Creates a new hero in the database.
    """
    # Create an instance of the Hero model
    employee = company(name=name, secret_name=secret_name, age=age)
    
    # Add the new hero to the session
    db.add(employee)
    
    # Commit the changes to the database
    db.commit()
    
    # Refresh the hero object to get the new ID from the database
    db.refresh(employee)
    
    # Return the created hero object as a JSON response
    return employee