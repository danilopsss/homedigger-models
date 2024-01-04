from enum import Enum

class Events(Enum):
    TOKEN_GENERATED = "TOKEN_GENERATED"
    TOKEN_REFRESHED = "TOKEN_REFRESHED"
    USER_CREATED = "USER_CREATED"
