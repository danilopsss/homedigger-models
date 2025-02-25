from sqlalchemy.orm import relationship
from sqlalchemy import (
    Column,
    String,
    Integer,
    Boolean,
    ForeignKey,
    UniqueConstraint,
)
from sqlalchemy.dialects.postgresql import UUID
from hdmdata.database._base_model import BaseModel


class Advertisements(BaseModel):
    __tablename__ = "advertisements"
    __table_args__ = (
        UniqueConstraint(
            "title",
            "link",
            "price",
            "parking",
            "rooms",
            "size",
            "floor",
            "rent_office_id",
        ),
        {"schema": "homedigger"},
    )

    title = Column(String(length=200), nullable=False)
    link = Column(String(length=200), nullable=False)
    price = Column(Integer, nullable=False)
    parking = Column(Boolean, default=False)
    rooms = Column(Integer, nullable=False)
    size = Column(Integer, nullable=False)
    floor = Column(Integer, nullable=False)

    rent_office_id = Column(UUID, ForeignKey("homedigger.rent_office.id"))
    rent_office = relationship(
        "RentOffice",
        lazy="subquery",
        uselist=False,
        back_populates="advertisements",
        cascade="merge",
    )
