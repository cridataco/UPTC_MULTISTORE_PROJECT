from sqlalchemy import Column, String, Integer, Date, ForeignKey
from sqlalchemy.orm import relationship
from .sql_base import Base


class Ratings(Base):
    __tablename__ = "ratings"

    id_order = Column(
        Integer, ForeignKey("orders.id_order"), primary_key=True, nullable=False
    )  # fk orders
    id_product = Column(
        Integer, ForeignKey("product.id_product"), primary_key=True, nullable=False
    )  # fk product
    rating = Column(Integer, nullable=False)
    comment = Column(String(1000), nullable=False)
    rating_date = Column(Date, nullable=False)
    rating_edit_date = Column(Date, nullable=True)
    rating_elimination_date = Column(Date, nullable=True)

    # Many ratings can be for One order
    order = relationship("Orders", back_populates="ratings")
    # Many ratings can be for One product
    product = relationship("Product", back_populates="ratings")

    def __init__(
        self,
        rating,
        comment,
        rating_date,
        rating_edit_date=None,
        rating_elimination_date=None,
    ):
        self.rating = rating
        self.comment = comment
        self.rating_date = rating_date
        self.rating_edit_date = rating_edit_date
        self.rating_elimination_date = rating_elimination_date