from fastapi import FastAPI
from app.routers import user, product, order
from app.database import Base, engine

# Initialize database
Base.metadata.create_all(bind=engine)

# Create FastAPI app
app = FastAPI()

# Include routers
app.include_router(user.router)
app.include_router(product.router)
app.include_router(order.router)

@app.get("/")
def read_root():
    return {"message": "Welcome to the E-commerce Backend!"}
