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
                session.merge(data)
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

    if not issubclass(type(by), by_):
        raise TypeError("`by` must be a subclass of QueryBy")

    if getattr(schema, "__by__", None):
        return STANDARD_STMT.where(
            getattr(schema.__orm_model__, by.column) == by.value
        )
    return STANDARD_STMT


def get_model_from_db(function):
    def wrapper(*args, **kwargs):
        schema = function(*args, **kwargs)
        with get_session() as session:
            stmt = get_by(schema=schema, by=schema.__by__)
            return session.execute(stmt).fetchall()

    return wrapper
