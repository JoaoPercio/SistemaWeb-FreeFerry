from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Crie um mecanismo (engine) PostgreSQL com as credenciais fornecidas
engine = create_engine("postgresql://percito:software1605.@postgresql.uhserver.com:5432/univali")

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()