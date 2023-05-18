from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

from src.core.config import env_settings

settings = env_settings()

engine = create_engine(
    settings.DATABASE_CONN_STRING,
    future=True,
)

SessionLocal = sessionmaker(autoflush=False, autocommit=False, bind=engine)


def get_db_conn():
    db = scoped_session(SessionLocal)
    try:
        yield db
    finally:
        db.close()
