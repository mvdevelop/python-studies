
from fastapi import APIRouter

router = APIRouter(prefix="/orders", tags=["Orders"])

orders = []

@router.post("/")
def create_order(product_id: int, quantity: int):

    new_order = {
        "id": len(orders) + 1,
        "product_id": product_id,
        "quantity": quantity
    }

    orders.append(new_order)

    return new_order


@router.get("/")
def list_orders():
    return orders
