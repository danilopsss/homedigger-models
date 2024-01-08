from pydantic import model_validator
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

    @model_validator(mode="before")
    def size_str_to_int(self):
        for attr in ["price", "rooms", "size"]:
            value = self.get(attr)
            normalized_value = Converter.extract_number_from_string(value)
            self[attr] = normalized_value
        return self
