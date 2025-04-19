from contextlib import asynccontextmanager
from fastapi import FastAPI
from models import OrderRequest, OrderStatus
from queue_manager import add_order, get_order_status, get_orders
from dispatcher import process_orders
import asyncio

app = FastAPI()


@asynccontextmanager
async def lifespan(app: FastAPI):
    task = asyncio.create_task(process_orders())
    yield
    task.cancel()

app = FastAPI(lifespan=lifespan)


@app.post("/order")
async def place_order(order: OrderRequest):
    order_id = add_order(order.model_dump())
    return {"order_id": order_id, "status": "queued"}


@app.get("/order/{order_id}", response_model=OrderStatus)
async def check_status(order_id: str):
    status = get_order_status(order_id)
    return {"order_id": order_id, "status": status}


@app.get("/orders")
async def get_all_orders():
    orders = get_orders()
    return {"orders": orders}


@app.get("/")
async def root():
    return {"status": "Api is running"}
