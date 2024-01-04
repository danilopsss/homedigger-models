from pydantic import field_validator
from hdmdata.models.enums.events import Events
from hdmdata.database._base_schema import BaseSchema
from hdmdata.models.users.user_access_history import UserAccessHistory


class UserAccessHistorySchema(BaseSchema):
    __orm_model__ = UserAccessHistory

    event: str
    ip: str
    user_agent: str

    @field_validator("event")
    def validate_event(cls, value):
        if value not in [enum.value for enum in Events]:
            raise ValueError(f"Event {value} is not valid")
        return value
