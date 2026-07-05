from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel

app = FastAPI()


class OrderPublic(BaseModel):
    id: int
    customer_name: str
    total_amount: float


orders_db = [
    {"id": 1, "customer_name": "Nguyen Van A", "total_amount": 1500000.0, "profit_margin": 0.25, "supplier_id": "SUP_DELL_01"},
    {"id": 2, "customer_name": "Tran Thi B", "total_amount": 350000.0, "profit_margin": 0.30, "supplier_id": "SUP_LOGI_02"}
]


@app.get("/orders/{order_id}", response_model=OrderPublic)
def get_order_detail(order_id: int):
    for order in orders_db:
        if order["id"] == order_id:
            return order  # FastAPI sẽ tự lọc bỏ profit_margin và supplier_id dựa vào OrderPublic
            

    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND, 
        detail="Order not found"
    )