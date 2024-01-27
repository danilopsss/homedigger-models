import re
from pydantic import model_validator
from hdmdata.utils.conversions import Converter
from hdmdata.utils.validators import has_valid_link
from hdmdata.database._base_schema import BaseSchema
from hdmdata.models.advertisements import Advertisements


class AdvertisementsSchema(BaseSchema):
    __orm_model__ = Advertisements

    title: str
    link: str
    price: int
    parking: bool
    rooms: int
    size: int
    floor: int


    @model_validator(mode="before")
    def size_str_to_int(self):
        for attr in ["price", "rooms", "size"]:
            value = self.get(attr)
            normalized_value = Converter.extract_number_from_string(value)
            self[attr] = normalized_value
        return self


    @model_validator(mode="before")
    def validate_link(self):
        if not has_valid_link(self.get("link", "")):
            raise ValueError("Invalid link format")
        return self


    @model_validator(mode="before")
    def extract_floor(self):
        floor = self.get("floor", "")
        ground_floor = re.compile(r"[bB]ajo", re.IGNORECASE)
        if ground_floor.match(str(floor)):
            self["floor"] = 0
        else:
            self["floor"] = Converter.extract_number_from_string(floor)
        return self
