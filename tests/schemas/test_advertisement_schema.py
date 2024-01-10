import pytest
from pydantic import ValidationError
from hdmdata.schemas.advertisements import AdvertisementsSchema
from hdmdata.schemas.advertisements import RentOfficeSchema


def test_advertising_schema(advertisement_data):
    rent_office = AdvertisementsSchema(**advertisement_data)
    assert type(rent_office) == AdvertisementsSchema

    advertisement_data.pop("title")
    with pytest.raises(ValidationError) as ve:
        AdvertisementsSchema(**advertisement_data)
    assert ve.value is not None


def test_rent_office_schema(rent_office_data):
    rent_office = RentOfficeSchema(**rent_office_data)
    assert type(rent_office) == RentOfficeSchema

    rent_office_data.pop("title")
    with pytest.raises(ValidationError) as ve:
        RentOfficeSchema(**rent_office_data)
    assert ve.value is not None


def test_rent_office_schema_conversion(advertisement_data_with_str_not_int):
    advert = AdvertisementsSchema(**advertisement_data_with_str_not_int)
    assert type(advert) == AdvertisementsSchema
    assert advert.size == 422
    assert advert.price == 550000
