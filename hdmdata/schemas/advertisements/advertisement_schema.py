from hdmdata.models.users.users_model import Users
from hdmdata.database._base_schema import BaseSchema


class AdvertisementsSchema(BaseSchema):
    __orm_model__ = Users

    title: str
    price: int
    parking: bool
    rooms: int
    size: int
