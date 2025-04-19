from pydantic import BaseModel
from typing import List

class OrderItem(BaseModel):
    item_name: str
    quantity: int

class OrderRequest(BaseModel):
    items: List[OrderItem]

class OrderStatus(BaseModel):
    order_id: str
    status: str  # queued, in_progress, completed