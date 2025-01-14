from dotenv import load_dotenv
import os

# Load environment variables from a .env file
load_dotenv()

class Config:
    """Configuration class for the application."""
    DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///ecommerce.db")
    SECRET_KEY = os.getenv("SECRET_KEY", "default_secret_key")
