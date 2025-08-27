
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

mysql_url = "mysql+mysqlconnector://root:Ansh7905$@localhost:3306/fastapi_db"
engine = create_engine(mysql_url, echo=True)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()
