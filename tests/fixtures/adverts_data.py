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

@pytest.fixture(autouse=True)
def rent_office_data(advertisement_data):
    return {
        "title": "title",
        "link": "link",
        "advertisements": [advertisement_data],
    }