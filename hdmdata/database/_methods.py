import logging
from ._session import get_session
from sqlalchemy import select
from sqlalchemy.exc import IntegrityError
from hdmdata.types.get_by_type import by_


def save_model_to_db(function):
    def wrapper(*args, **kwargs):
        data = function(*args, **kwargs)
        with get_session() as session:
            try:
                session.begin()
                session.add(data)
                session.commit()
            except IntegrityError:
                session.rollback()
                session.close()
                logging.warning("Duplicated entry, rolling back.")
        return data

    return wrapper


def get_by(*, schema, by: None | by_):
    STANDARD_STMT = select(schema.__orm_model__)

    if not by:
        return STANDARD_STMT

    if not issubclass(by, by_):
        raise TypeError("`by` must be a subclass of QueryBy")

    if query_by := getattr(schema, "by", None):
        if hasattr(query_by, "id"):
            return STANDARD_STMT.where(schema.__orm_model__.id == query_by.id)
        if hasattr(query_by, "name"):
            return STANDARD_STMT.where(
                schema.__orm_model__.name == query_by.name
            )


def get_model_from_db(function):
    def wrapper(*args, **kwargs):
        schema = function(*args, **kwargs)
        with get_session() as session:
            stmt = get_by(schema=schema, by=schema.__by__)
            return session.execute(stmt).fetchall()

    return wrapper
