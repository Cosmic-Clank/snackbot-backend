from arm_controller import ArmController
import asyncio

popcorn_arm = ArmController(robot_model="wx250", robot_name="arm1")
drink_arm = ArmController(robot_model="wx250", robot_name="arm2")


async def handle_popcorn(item):
    if "regular popcorn" in item:
        popcorn_arm.make_regularpopcorn()
    elif "kettlecorn" in item:
        popcorn_arm.make_kettlecorn()


async def handle_drink(item):
    if "coffee" in item:
        drink_arm.make_coffee()
    elif "grape" in item:
        drink_arm.make_grape_juice()
    elif "apple" in item:
        drink_arm.make_apple_juice()
    elif "cranberry" in item:
        drink_arm.make_cranberry_juice()


async def send_to_robot(order):
    print(f"[🤖] Starting order {order['order_id']}")

    items = order['data']['items'].lower()
    tasks = []

    # Add popcorn task
    if "regular popcorn" in items or "kettlecorn" in items:
        tasks.append(handle_popcorn(items))

    # Add drink task
    if any(drink in items for drink in ["coffee", "grape", "apple", "cranberry"]):
        tasks.append(handle_drink(items))

    # Run both in parallel
    await asyncio.gather(*tasks)

    print(f"[✅] Completed order {order['order_id']}")
