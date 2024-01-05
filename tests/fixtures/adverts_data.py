import pytest


@pytest.fixture
def advertisement_data():
    return {
        "title": "title",
        "price": 100,
        "parking": True,
        "rooms": 1,
        "size": 100,
    }

@pytest.fixture
def advertisement_data_with_str_not_int():
    return {
        "title": "title",
        "price": "15464",
        "parking": True,
        "rooms": 1,
        "size": "422 m²",
    }

@pytest.fixture(autouse=True)
def rent_office_data(advertisement_data):
    return {
        "title": "title",
        "link": "link",
        "advertisements": [advertisement_data],
    }
