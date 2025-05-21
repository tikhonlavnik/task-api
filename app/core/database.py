from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from config import settings

engine = create_engine(settings.SQL_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, bind=engine)

Base = declarative_base()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def recreate_db():
    metadata = Base.metadata
    metadata.reflect(bind=engine)

    metadata.drop_all(bind=engine)
    print("All tables dropped")

    Base.metadata.create_all(bind=engine)
    print("All tables created")
