from hdmdata.database._base_schema import BaseSchema
from hdmdata.models.users.user_secrets import UserSecrets


class UsersSecretsSchema(BaseSchema):
    __orm_model__ = UserSecrets

    secret: str
    salt: str
    personal_key: str
