from sqlalchemy import Column, Integer, ForeignKey, String, Sequence, Numeric
from sqlalchemy.orm import relationship
from .order_itemModel import OrderItem


from config.db_config import Base


class Item(Base):
    __tablename__ = 'product'

    id_product = Column(Integer, Sequence('id_prod_seq'), primary_key=True)
    id_category = Column(Integer, ForeignKey('category.id_category', ondelete='SET NULL', onupdate='CASCADE'),
                       nullable=False)
    product_name = Column(String(63), nullable=False)
    cost = Column(Numeric(12, 2), nullable=False)
    product = relationship(OrderItem, passive_updates=True, backref="product.id_product")

    def __init__(self, id_category, product_name, cost):
        self.id_category = id_category
        self.product_name = product_name,
        self.cost = cost
