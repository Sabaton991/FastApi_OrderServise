from fastapi import APIRouter, Depends, status, HTTPException, Response
from config.db_config import get_db
from sqlalchemy.orm import Session
from processes.itemsDb import ItemsDb
from schemas.itemSchemas import ItemAdd

router = APIRouter(
    tags=['Items'],
    prefix='/items'
)


@router.get('/')
def get_all_items(db: Session = Depends(get_db)):
    a = ItemsDb(db).get_all_items(limit=10)
    return a


@router.post('/create_item', status_code=status.HTTP_201_CREATED)
def create_item(request: ItemAdd, response: Response, db: Session = Depends(get_db)):
    if ItemsDb(db).create_item(request.id_category, request.product_name, request.cost):
        return {'data': 'Ok'}
    else:
        response.status_code = status.HTTP_400_BAD_REQUEST
        return {'data': 'BAD'}