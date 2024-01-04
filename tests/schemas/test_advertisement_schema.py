import pytest
from pydantic import ValidationError
from hdmdata.schemas.advertisements.advertisement_schema import AdvertisementsSchema
from hdmdata.schemas.advertisements.rent_office_schema import RentOfficeSchema


def test_advertising_schema(advertisement_data):
    user = AdvertisementsSchema(**advertisement_data)
    assert type(user) == AdvertisementsSchema

    advertisement_data.pop("title")
    with pytest.raises(ValidationError) as ve:
        AdvertisementsSchema(**advertisement_data)
    assert ve.value is not None


def test_rent_office_schema(rent_office_data):
    user = RentOfficeSchema(**rent_office_data)
    assert type(user) == RentOfficeSchema

    rent_office_data.pop("title")
    with pytest.raises(ValidationError) as ve:
        RentOfficeSchema(**rent_office_data)
    assert ve.value is not None