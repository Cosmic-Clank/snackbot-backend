from contextlib import asynccontextmanager
from fastapi import FastAPI
from models import OrderRequest, OrderStatus
from queue_manager import add_order, get_order_status, get_orders, get_current_order
from dispatcher import process_orders
from fastapi.middleware.cors import CORSMiddleware
import asyncio

app = FastAPI()


@asynccontextmanager
async def lifespan(app: FastAPI):
    task = asyncio.create_task(process_orders())
    yield
    task.cancel()

app = FastAPI(lifespan=lifespan)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Adjust to your frontend's origin
    allow_credentials=True,
    allow_methods=["*"],  # Allow all methods (GET, POST, OPTIONS, etc.)
    allow_headers=["*"],  # Allow all headers (Content-Type, etc.)
)


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
    current = get_current_order()
    return {"current_order": current, "queued_orders": orders}


@app.get("/")
async def root():
    return {"status": "Api is running"}
