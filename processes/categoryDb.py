from db_models.categoryModel import Category
from sqlalchemy.orm import Session


class CategoryDb:
    def __init__(self, db: Session):
        self.session = db

    def get_all_categories(self):
        self.session.query(Category).all()


