from sqlalchemy.orm import relationship
from sqlalchemy import Column, String
from hdmdata.database._base_model import BaseModel


class RentOffice(BaseModel):
    __tablename__ = 'rent_office'

    title = Column(String(length=200), nullable=False)
    link = Column(String(length=100), nullable=False)
    
    advertisements = relationship(
       "Advertisements", 
        lazy=True,
        uselist=True,
        back_populates="rent_office",
    )
