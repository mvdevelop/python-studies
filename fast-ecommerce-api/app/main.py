
from fastapi import FastAPI
from app.controllers import product_controller, order_controller

app = FastAPI(title="Ecommerce API")

app.include_router(product_controller.router)
app.include_router(order_controller.router)

@app.get("/")
def root():
    return {"message": "Ecommerce API running"}
