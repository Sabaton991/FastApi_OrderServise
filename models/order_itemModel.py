from sqlalchemy import Column, Integer, String, Sequence, ForeignKey
from sqlalchemy.orm import relationship
from config.db_config import Base


class OrderItem(Base):
    __tablename__ = 'order_item'

    id_order_item = Column(Integer, Sequence('id_ord_item_seq'), primary_key=True)
    id_product = Column(ForeignKey('product.id_product', ondelete='SET NULL', onupdate='CASCADE'), nullable=False)
    id_order = Column(ForeignKey('order.id_order', ondelete='SET NULL', onupdate='CASCADE'), nullable=False)
    item_count = Column(Integer, nullable=False)

    def __init__(self, id_product, item_count):
        self.id_product = id_product
        self.item_count = item_count