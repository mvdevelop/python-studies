
from fastapi import APIRouter
from app.models.product_model import Product
from app.views.product_view import ProductCreate

router = APIRouter(prefix="/products", tags=["Products"])

products = []

@router.post("/")
def create_product(product: ProductCreate):
    new_product = {
        "id": len(products) + 1,
        "name": product.name,
        "price": product.price,
        "stock": product.stock
    }

    products.append(new_product)
    return new_product


@router.get("/")
def list_products():
    return products
