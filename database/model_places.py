from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Places(Base):
    __tablename__ = "places"

    id_place = Column(Integer, primary_key=True, autoincrement=True)  # pk id
    id_location = Column(
        Integer, ForeignKey("places.id_location"), nullable=True, autoincrement=True
    )  # fk places
    place_name = Column(String(50), nullable=False)
    place_type = Column(String(7), nullable=False)
    postal_code = Column(Integer, nullable=False)
    
    shipping_address = relationship("ShippingAddress")
    #Recursividad consigo misma
    sublocations = relationship("Places", remote_side=[id_place])

    def __init__(self, place_name, place_type, postal_code):
        self.place_name = place_name
        self.place_type = place_type
        self.postal_code = postal_code
