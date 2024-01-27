from sqlalchemy.orm import relationship
from sqlalchemy import Column, String, UniqueConstraint
from hdmdata.database._base_model import BaseModel


class RentOffice(BaseModel):
    __tablename__ = "rent_office"
    __table_args__ = (
        UniqueConstraint("title", "link"),
        {"schema": "homedigger"},
    )

    title = Column(String(length=200), nullable=False)
    link = Column(String(length=100), nullable=False)

    advertisements = relationship(
        "Advertisements",
        lazy="subquery",
        uselist=True,
        back_populates="rent_office",
        cascade="merge",
    )
