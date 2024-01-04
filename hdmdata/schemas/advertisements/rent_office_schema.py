from typing import Optional, List
from hdmdata.models.advertisements.rent_office import RentOffice
from .advertisement_schema import AdvertisementsSchema
from hdmdata.database._base_schema import BaseSchema


class RentOfficeSchema(BaseSchema):
    __orm_model__ = RentOffice

    title: str
    link: str
    advertisements: Optional[List[AdvertisementsSchema]] = None

