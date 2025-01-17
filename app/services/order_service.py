from sqlalchemy.orm import Session
from app.models.order import Order
from app.schemas.order import OrderCreate


def create_order(db: Session, order: OrderCreate) -> Order:
    db_order = Order(user_id=order.user_id, product_id=order.product_id, quantity=order.quantity, total_price=order.total_price)
    db.add(db_order)
    db.commit()
    db.refresh(db_order)
    return db_order


def get_order(db: Session, order_id: int) -> Order:
    return db.query(Order).filter(Order.id == order_id).first()
