from fastapi import APIRouter
from bson.objectid import ObjectId

from models.product_schemas import ProductSchema
from models.products import Product

router = APIRouter(prefix="/products", tags=["products"])


@router.get("/", response_model=None)
async def list_products():
    products = Product.objects().to_json()  # MongoEngine provides .to_json()
    return products


@router.get("/{id}", response_model=None)
async def list_product(id: str):
    product = Product.objects(id=ObjectId(id)).first()
    if product:
        return product.to_json()  # MongoEngine provides .to_json()
    return None


@router.post("/", response_model=None)
async def create_product(product: ProductSchema):
    product = Product(**product.model_dump())
    product.save()  # MongoEngine's save method
    return {"item_id": str(product.id)}
