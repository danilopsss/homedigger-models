from sqlalchemy.types import Enum
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy import Column, String, ForeignKey

from hdmdata.database._base_model import BaseModel
from ..enums.events import Events


class UserAccessHistory(BaseModel):
    __tablename__ = "user_access_history"

    event: String = Column(Enum(Events), nullable=False)
    ip: String = Column(String, nullable=False)
    user_agent: String = Column(String(100), nullable=False)

    user_id = Column(UUID, ForeignKey("user.id"))
    user = relationship(
        "Users", lazy=True, uselist=False, back_populates="access_history"
    )
