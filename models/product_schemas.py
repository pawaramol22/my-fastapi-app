from pydantic import BaseModel


class ProductSchema(BaseModel):  # For API schema
    name: str
    description: str = None
    price: float