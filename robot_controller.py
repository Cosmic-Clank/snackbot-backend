from interbotix_xs_modules.arm import InterbotixManipulatorXS
from recipies import *
from threading import Thread
import asyncio
import rospy

popcorn_bot = InterbotixManipulatorXS(
    robot_model="wx250", robot_name="arm_1", init_node=False)
drink_bot = InterbotixManipulatorXS(
    robot_model="wx250", robot_name="arm_2", init_node=False)


def handle_popcorn(items):
    if "regular popcorn" in items:
        make_regularpopcorn(popcorn_bot)
    elif "kettlecorn" in items:
        make_kettlecorn(popcorn_bot)


def handle_drink(items):
    if "coffee" in items:
        make_coffee(drink_bot)
    elif "grape juice" in items:
        make_grape_juice(drink_bot)
    elif "apple juice" in items:
        make_apple_juice(drink_bot)
    elif "cranberry juice" in items:
        make_cranberry_juice(drink_bot)


async def send_to_robot(order):
    print(f"[🤖] Starting order {order['order_id']}")
    items = [item['item_name'].lower() for item in order['data']['items']]
    threads = []

    if "regular popcorn" in items or "kettlecorn" in items:
        threads.append(Thread(target=handle_popcorn, args=(items,)))

    if any(drink in items for drink in ["coffee", "grape juice", "apple juice", "cranberry juice"]):
        threads.append(Thread(target=handle_drink, args=(items,)))

    rospy.init_node("xsarm_dual")
    for t in threads:
        t.start()

    # Now block until they're all done, but do it in async-friendly way
    await asyncio.get_event_loop().run_in_executor(None, lambda: [t.join() for t in threads])

    print(f"[✅] Completed order {order['order_id']}")
