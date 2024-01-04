import os
import sqlalchemy

from contextlib import contextmanager
from sqlalchemy.orm import sessionmaker


def __get_url():
    return "%s://%s:%s@%s/%s" % (
        os.environ.get("DB_PROVIDER", "postgresql"),
        os.environ.get("DB_USER", "DB_USER"),
        os.environ.get("DB_PASSWORD", "DB_PASSWORD"),
        os.environ.get("DB_HOST", "localhost"),
        os.environ.get("DB_DB", "DB_DB"),
    )

def __db_session():
    db_url = __get_url()
    engine = sqlalchemy.create_engine(db_url)
    return sessionmaker(bind=engine, autoflush=True)()


@contextmanager
def get_session():
    with __db_session() as session:
        yield session
