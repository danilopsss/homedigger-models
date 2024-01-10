import pytest
from datetime import datetime


@pytest.fixture
def user_secrets():
    return {"secret": "secret", "salt": "salt", "personal_key": "personal_key"}


@pytest.fixture
def user_details():
    return {"name": "name", "birthday": datetime(2021, 1, 1), "email": "email"}


@pytest.fixture(autouse=True)
def user_data(user_details, user_secrets):
    return {
        "username": "username",
        "details": user_details,
        "secrets": user_secrets,
    }
