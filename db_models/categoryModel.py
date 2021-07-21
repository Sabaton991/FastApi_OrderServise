from sqlalchemy import Column, Integer, String, Sequence
from sqlalchemy.orm import relationship
from config.db_config import Base
from .itemModel import Item


class Category(Base):
    __tablename__ = 'category'

    id_category = Column(Integer, Sequence('id_cat_seq'), primary_key=True)
    category_name = Column(String(31), nullable=False)
    category = relationship(Item, passive_updates=True, backref="category.id_category")

    def __init__(self, name):
        self.category_name = name
