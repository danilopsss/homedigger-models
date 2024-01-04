import pytest
from pydantic import ValidationError
from hdmdata.schemas.users.users_schema import UserSchema
from hdmdata.schemas.users.users_details_schema import UsersDetailsSchema
from hdmdata.schemas.users.users_secrets_schema import UsersSecretsSchema


def test_user_schema(user_data):
    user = UserSchema(**user_data)
    assert type(user) == UserSchema
    assert type(user.details) == UsersDetailsSchema
    assert type(user.secrets) == UsersSecretsSchema

    user_data.pop("details")
    with pytest.raises(ValidationError) as ve:
        UserSchema(**user_data)
    assert ve.value is not None
