from sqlalchemy import Column, Integer, ForeignKey, String, Float
from sqlalchemy.orm import relationship
from app.database import Base

class Order(Base):
    __tablename__ = "orders"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    product_id = Column(Integer, ForeignKey("products.id"), nullable=False)
    quantity = Column(Integer, nullable=False)
    total_price = Column(Float, nullable=False)
    status = Column(String, default="pending")

    user = relationship("User", back_populates="orders")
    product = relationship("Product", back_populates="orders")

# Add relationships in the related models
User.orders = relationship("Order", back_populates="user", cascade="all, delete-orphan")
Product.orders = relationship("Order", back_populates="product", cascade="all, delete-orphan")
