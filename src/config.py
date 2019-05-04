# Configuration module for StockFlow Enterprise Inventory & Warehouse ERP
import os
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    app_name: str = "StockFlow Enterprise Inventory & Warehouse ERP"
    port: int = int(os.getenv("PORT", "8080"))
    database_url: str = os.getenv("DATABASE_URL", "postgresql://postgres:postgres@localhost:5432/stockflow_django_erp_db")
    redis_url: str = os.getenv("REDIS_URL", "redis://localhost:6379/0")

settings = Settings()
