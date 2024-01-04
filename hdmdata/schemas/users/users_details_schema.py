from datetime import datetime
from hdmdata.database._base_schema import BaseSchema
from hdmdata.models.users.user_details import UserDetails


class UsersDetailsSchema(BaseSchema):
    __orm_model__ = UserDetails

    name: str
    birthday: datetime
    email: str
