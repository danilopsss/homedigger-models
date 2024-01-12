from pydantic import model_validator
from hdmdata.utils.validators import has_valid_link
from hdmdata.database._base_schema import BaseSchema
from hdmdata.models.advertisements import Advertisements


class AdvertisementsMainLinkSchema(BaseSchema):
    __orm_model__ = Advertisements

    link: str
    visited: bool = False

    @model_validator(mode="before")
    def validate_link(self):
        if not has_valid_link(self.get("link", "")):
            raise ValueError("Invalid link format")
        return self
