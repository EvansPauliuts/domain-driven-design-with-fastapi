from sqlalchemy.ext.declarative import declarative_base

from src.core.db import engine

EntityMeta = declarative_base()


def init():
    EntityMeta.metadata.create_all(bind=engine)
