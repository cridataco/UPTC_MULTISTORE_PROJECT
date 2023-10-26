from sqlalchemy import Column, Integer, String, Date, ForeignKey
from sqlalchemy.orm import relationship
from .sql_base import Base


class Product(Base):
    __tablename__ = "product"

    id_product = Column(Integer, primary_key=True, autoincrement=True)  # pk id
    id_tax = Column(Integer, ForeignKey("taxes.id_tax"), nullable=False) # fk taxes
    product_name = Column(String(50), nullable=False)
    reference_model = Column(String(50), nullable=False)
    summary_description = Column(String(100), nullable=False)
    release_date = Column(Date, nullable=False)
    creation_date = Column(Date, nullable=False)
    key_words = Column(String(100), nullable=True)
    product_link = Column(String(500), nullable=True)
    
    #Many products can have One tax
    tax = relationship("Taxes", back_populates="products")
    #One product can have Many resources
    resources = relationship("Resources", back_populates="product")
    classifications = relationship("Classification")
    product_stock = relationship("ProductStock")
    price_history = relationship("PriceHistory")
    ratings = relationship("Ratings")
    product_features = relationship("ProductFeatures")

    