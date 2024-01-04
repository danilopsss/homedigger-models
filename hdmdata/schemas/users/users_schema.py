from typing import List, Optional
from hdmdata.models.users.users_model import Users
from hdmdata.database._base_schema import BaseSchema
from hdmdata.schemas.users.users_details_schema import UsersDetailsSchema
from hdmdata.schemas.users.users_secrets_schema import UsersSecretsSchema
from hdmdata.schemas.users.users_access_history import UserAccessHistorySchema


class UserSchema(BaseSchema):
    __orm_model__ = Users

    username: str
    details: UsersDetailsSchema
    secrets: UsersSecretsSchema
    access_history: Optional[List[UserAccessHistorySchema]] = None
