from typing import Optional

from fastapi import APIRouter, Depends, status, HTTPException, Response
from config.db_config import get_db
from sqlalchemy.orm import Session
from processes.itemsDb import ItemsDb
from schemas.itemSchemas import ItemAdd, ItemCategory, ItemPosition, LimitOffset

router = APIRouter(
    tags=['Items'],
    prefix='/items'
)


@router.get('/', status_code=status.HTTP_200_OK)
def get_all_items(limit: Optional[int] = None, db: Session = Depends(get_db)):
    if limit is None:
        records = ItemsDb(db).get_all_items(limit=10)
        if records:
            return records
        else:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail='No records')
    else:
        records = ItemsDb(db).get_all_items(limit=limit)
        if records:
            return records
        else:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail='No records')


@router.post('/create_item', status_code=status.HTTP_201_CREATED)
def create_item(request: ItemAdd, response: Response, db: Session = Depends(get_db)):
    if ItemsDb(db).create_item(request.id_category, request.product_name, request.cost):
        return {'data': 'Ok'}
    else:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail='Cannot create item')


@router.post('/get_item_category', status_code=status.HTTP_200_OK)
def get_all_items_category(request: LimitOffset, response: Response, db: Session = Depends(get_db)):
    records = ItemsDb(db).get_all_items_with_categories(request.offset)
    if records:
        return records
    else:
        response.status_code = status.HTTP_400_BAD_REQUEST
        return {'detail': 'No records'}