from sqlalchemy.orm import Session
from db_models.itemModel import Item
from config.logging_config import logging


class ItemsDb:

    def __init__(self, db: Session):
        self.session = db

    def get_all_items(self, limit):
        all_records = self.session.query(Item).limit(limit).all()
        return all_records

    def create_item(self, id_category, product_name, cost):
        try:
            logging.info('creating...')
            self.session.add(Item(id_category=id_category, product_name=product_name, cost=cost))
            self.session.commit()
            return True
        except Exception as err:
            self.session.rollback()
            logging.error(err)
            return False