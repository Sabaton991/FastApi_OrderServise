from sqlalchemy import Column, Integer, String, Sequence, Numeric
from config.db_config import Base
from sqlalchemy.orm import relationship
from .order_itemModel import OrderItem


class Order(Base):
    __tablename__ = 'order'

    id_order = Column(Integer, Sequence('id_order_seq'), primary_key=True)
    status = Column(String(15), nullable=False, default='Not open')
    final_cost = Column(Numeric(12, 2), nullable=False)
    order = relationship(OrderItem, passive_updates=True,
                            backref="order")

    def __init__(self, final_cost):
        self.final_cost = final_cost