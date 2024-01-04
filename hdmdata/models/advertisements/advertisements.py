from sqlalchemy.orm import relationship
from sqlalchemy import Column, String, Integer, Boolean, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from hdmdata.database._base_model import BaseModel


class Advertisements(BaseModel):
    __tablename__ = 'advertisements'

    title = Column(String(length=200), nullable=False)
    price = Column(Integer, nullable=False, max_length=10)
    parking = Column(Boolean, default=False)
    rooms = Column(Integer, nullable=False)
    size = Column(Integer, nullable=False)
    
    rent_office_id = Column(UUID, ForeignKey('rent_office.id'))
    rent_office = relationship(
        "RentOffice",
        lazy=True,
        uselist=False,
        back_populates="advertisements"
    )
