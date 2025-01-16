from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.schemas.order import OrderCreate, OrderResponse
from app.models.order import Order
from app.database import get_db
from app.services.order_service import create_order, get_order

router = APIRouter(prefix="/orders", tags=["Orders"])

@router.post("/", response_model=OrderResponse)
def place_order(order: OrderCreate, db: Session = Depends(get_db)):
    db_order = create_order(db, order)
    return db_order

@router.get("/{order_id}", response_model=OrderResponse)
def retrieve_order(order_id: int, db: Session = Depends(get_db)):
    return get_order(db, order_id)
