from fastapi import FastAPI, Depends, APIRouter
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker, declarative_base, Session

# --- 1. Database Setup ---
# Define the database file and create an engine
sqlite_file_name = "database.db"
sqlite_url = f"sqlite:///{sqlite_file_name}"

# The engine manages the database connection
engine = create_engine(sqlite_url, connect_args={"check_same_thread": False})

# The base class for our models
Base = declarative_base()

# A factory to create new database sessions
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


# --- 2. Database Model ---
# This class represents the 'heroes' table
class Hero(Base):
    __tablename__ = "heroes"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    secret_name = Column(String)
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

# This event runs once at startup to create the database file and table
@app.on_event("startup")
def on_startup():
    create_db_and_tables()


# --- 5. API Endpoint to Add Data ---
@app.post("/heroes/")
def create_hero(name: str, secret_name: str, age: int, db: Session = Depends(get_db)):
    """
    Creates a new hero in the database.
    """
    # Create an instance of the Hero model
    hero = Hero(name=name, secret_name=secret_name, age=age)
    
    # Add the new hero to the session
    db.add(hero)
    
    # Commit the changes to the database
    db.commit()
    
    # Refresh the hero object to get the new ID from the database
    db.refresh(hero)
    
    # Return the created hero object as a JSON response
    return hero