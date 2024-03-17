from fastapi import FastAPI
import mongoengine
import certifi

from config import settings
from apps.products.routers import router as product_routers

app = FastAPI()

@app.on_event("startup")
async def startup_db_client():
    mongoengine.connect(db=settings.DB_NAME, host=settings.DB_URL, tlsCAFile=certifi.where())  # Use the instance

@app.on_event("shutdown")
async def shutdown_db_client():
    pass

app.include_router(product_routers, prefix="/api/1")
