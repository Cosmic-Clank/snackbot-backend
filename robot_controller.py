import asyncio

async def send_to_robot(order):
    print(f"[🤖] Starting order {order['order_id']}")
    await asyncio.sleep(5)  # Simulate time taken to prepare the order
    print(f"[✅] Completed order {order['order_id']}")