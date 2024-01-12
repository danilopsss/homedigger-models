import os
import sqlalchemy

from contextlib import contextmanager
from sqlalchemy.orm import sessionmaker


def __get_url():
    db_envvars = [
        "DB_PROVIDER",
        "DB_USER",
        "DB_PASSWORD",
        "DB_HOST",
        "DB_PORT",
        "DB_DB",
    ]

    for envvar in db_envvars:
        if not os.environ.get(envvar):
            raise ValueError(f"{envvar.split('_')[-1]} is not set")

    return "%s://%s:%s@%s:%s/%s" % (
        os.environ.get("DB_PROVIDER"),
        os.environ.get("DB_USER"),
        os.environ.get("DB_PASSWORD"),
        os.environ.get("DB_HOST"),
        os.environ.get("DB_PORT"),
        os.environ.get("DB_DB"),
    )


def __db_session():
    db_url = __get_url()
    engine = sqlalchemy.create_engine(db_url, echo=True)
    return sessionmaker(bind=engine, autoflush=True)()


@contextmanager
def get_session():
    with __db_session() as session:
        yield session
