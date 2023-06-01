from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base  # type: ignore

engine = create_engine("mysql+mysqlconnector://root:@localhost/mydb")

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()