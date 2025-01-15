from pydantic import BaseModel
from typing import List

class OrderBase(BaseModel):
    user_id: int
    product_id: int
    quantity: int
    total_price: float

class OrderCreate(OrderBase):
    pass

class OrderResponse(OrderBase):
    id: int
    status: str

    class Config:
        orm_mode = True
