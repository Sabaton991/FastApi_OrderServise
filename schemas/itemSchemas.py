from pydantic import BaseModel
from typing import Optional
# class itemRequest(BaseModel)

class Item(BaseModel):
    product_name: str
    cost: float
    id_item: int


class Category(BaseModel):
    id_category: str
    category_name: str


class ItemAdd(BaseModel):
    class Config:
        orm_mode = True

    product_name: str
    cost: float
    id_category: int

class LimitOffset(BaseModel):
    offset: int
    limit: Optional[int]


class ItemCategory(Item, Category):

    class Config:
        orm_mode = True

    item: Item
    category: Category


class ItemPosition(ItemCategory):
    id_product: int
    item_count: int

    class Config:
        orm_mode = True
