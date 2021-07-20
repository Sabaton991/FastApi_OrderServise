from pydantic import BaseModel


class ItemAdd(BaseModel):
    product_name: str
    cost: float
    id_category: int