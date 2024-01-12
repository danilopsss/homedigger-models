from typing import Optional, List
from hdmdata.models.advertisements.rentoffice_model import RentOffice
from .advert_schema import AdvertisementsSchema
from hdmdata.database._base_schema import BaseSchema


class RentOfficeSchema(BaseSchema):
    __orm_model__ = RentOffice

    title: str
    link: str
    advertisements: Optional[List[AdvertisementsSchema]] = None
