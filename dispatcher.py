import asyncio
from queue_manager import get_next_order, update_order_status
from robot_controller import send_to_robot


async def process_orders():
    while True:
        order = get_next_order()
        if order:
            order_id = order["order_id"]
            update_order_status(order_id, "in_progress")
            await send_to_robot(order)
            update_order_status(order_id, "completed")
        await asyncio.sleep(1)
