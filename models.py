from sqlalchemy import Column, Integer, String, Sequence, Numeric, ForeignKey, Table, TIMESTAMP
from sqlalchemy.orm import relationship, backref
from config.db_config import Base
import datetime


class Addresses(Base):
    __tablename__ = 'addresses_1'

    id_address = Column(Integer, Sequence('id_addr_seq'), primary_key=True)
    country = Column(String(31), nullable=False)
    city = Column(String(31), nullable=False)
    street = Column(String(31), nullable=False)
    number = Column(String(7), nullable=False)

    def __init__(self, country, city, street, number):
        self.country = country
        self.city = city
        self.street = street
        self.number = number


class OrderItem(Base):
    __tablename__ = 'order_item'

    id_order_item = Column(Integer, Sequence('id_ord_item_seq'), primary_key=True)
    id_product = Column(ForeignKey('product.id_product', ondelete='SET NULL', onupdate='CASCADE'), nullable=False)
    id_order = Column(ForeignKey('order.id_order', ondelete='SET NULL', onupdate='CASCADE'), nullable=False)
    item_count = Column(Integer, nullable=False)

    def __init__(self, id_product, item_count):
        self.id_product = id_product
        self.item_count = item_count


class Order(Base):
    __tablename__ = 'order'

    id_order = Column(Integer, Sequence('id_order_seq'), primary_key=True)
    status = Column(String(15), nullable=False, default='Not open')
    final_cost = Column(Numeric(12, 2), nullable=False)
    order = relationship(OrderItem, passive_updates=True,
                            backref="order")

    def __init__(self, final_cost):
        self.final_cost = final_cost


class Item(Base):
    __tablename__ = 'product'

    id_product = Column(Integer, Sequence('id_prod_seq'), primary_key=True)
    id_category = Column(Integer, ForeignKey('category.id_category', ondelete='SET NULL', onupdate='CASCADE'),
                       nullable=False)
    product_name = Column(String(63), nullable=False)
    cost = Column(Numeric(12, 2), nullable=False)
    product = relationship(OrderItem, passive_updates=True,
                            backref="product")

    def __init__(self, id_category, product_name, cost):
        self.id_category = id_category
        self.product_name = product_name,
        self.cost = cost

class Category(Base):
    __tablename__ = 'category'

    id_category = Column(Integer, Sequence('id_cat_seq'), primary_key=True)
    category_name = Column(String(31), nullable=False)
    category = relationship(Item, passive_updates=True,
                          backref="category")

    def __init__(self, name):
        self.category_name = name


address_user_table = Table('address_user', Base.metadata, Column('user_id', Integer, ForeignKey('user.id_user')),
                           Column('address_id', Integer, ForeignKey('addresses.id_address')))


class User(Base):
    __tablename__ = 'user'

    id_user = Column(Integer, Sequence('id_user_seq'), primary_key=True)
    password = Column(String(255), nullable=False)
    surname = Column(String(63), nullable=False)
    name = Column(String(63), nullable=False)
    patronymic = Column(String(63), nullable=True)
    gender = Column(String(63), nullable=False)
    phone = Column(String(63), nullable=True)
    created_at = Column(TIMESTAMP, nullable=False, default=datetime.datetime.now())
    email = Column(String, nullable=False)
    subs = relationship(Addresses, secondary=address_user_table, backref=backref('addr'), lazy='dynamic')

    def __init__(self, password, surname, name, last_name, gender, phone, email):
        self.password = password
        self.surname = surname
        self.name = name
        self.last_name = last_name
        self.gender = gender
        self.phone = phone
        self.email = email