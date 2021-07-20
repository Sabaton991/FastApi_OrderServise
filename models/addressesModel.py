from sqlalchemy import Column, Integer, String, Sequence
from config.db_config import Base


class Addresses(Base):
    __tablename__ = 'addresses'

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


