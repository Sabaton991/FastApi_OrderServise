from sqlalchemy import Column, Integer, String, Date, TIMESTAMP, Text, ForeignKey, Sequence, Table
from sqlalchemy.orm import relationship, backref
import datetime
from config.db_config import Base
from .addressesModel import Addresses

address_user_table = Table('address_user', Base.metadata, Column('user_id', Integer, ForeignKey('user.id_user')),
                           Column('address_id', Integer, ForeignKey('addresses.id_address')))


class User(Base):
    __tablename__ = 'user'

    id_user = Column(Integer, Sequence('id_user_seq'), primary_key=True)
    hashed_password = Column(String(255), nullable=False)
    surname = Column(String(63), nullable=False)
    name = Column(String(63), nullable=False)
    patronymic = Column(String(63), nullable=True)
    gender = Column(String(63), nullable=False)
    phone = Column(String(63), nullable=True)
    created_at = Column(TIMESTAMP, nullable=False, default=datetime.datetime.now())
    email = Column(String, nullable=False)
    subs = relationship(Addresses, secondary=address_user_table, backref=backref('addr'), lazy='dynamic')

    def __init__(self, hashed_password, surname, name, last_name, gender, phone, email):
        self.hashed_password = hashed_password
        self.surname = surname
        self.name = name
        self.last_name = last_name
        self.gender = gender
        self.phone = phone
        self.email = email



