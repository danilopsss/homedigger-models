from sqlalchemy import (
    Column,
    String,
    Boolean,
    UniqueConstraint,
)
from hdmdata.database._base_model import BaseModel


class AdvertisementsMainLink(BaseModel):
    __tablename__ = "advertisements_mainlink"
    __table_args__ = (
        UniqueConstraint("link"),
        {"schema": "homedigger"},
    )

    link = Column(String, nullable=False)
    visited = Column(Boolean, default=False, nullable=False)
