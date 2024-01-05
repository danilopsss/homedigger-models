from pydantic import validator
from hdmdata.models.advertisements import Advertisements
from hdmdata.database._base_schema import BaseSchema
from hdmdata.utils.conversions import Converter


class AdvertisementsSchema(BaseSchema):
    __orm_model__ = Advertisements

    title: str
    price: int
    parking: bool
    rooms: int
    size: int

    @validator("size", "rooms", "price", pre=True)
    def size_str_to_int(cls, value):
        return Converter.extract_number_from_string(value)
