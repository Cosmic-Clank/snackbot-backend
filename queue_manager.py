import queue
import uuid

order_queue = queue.Queue()
order_status = {}


def add_order(order_data):
    order_id = str(uuid.uuid4())
    order = {
        "order_id": order_id,
        "status": "queued",
        "data": order_data
    }
    order_queue.put(order)
    order_status[order_id] = "queued"
    print("order added to queue:", order)
    print("order queue: ", list(order_queue.queue))
    return order_id


def get_next_order():
    if not order_queue.empty():
        return order_queue.get()
    return None


def update_order_status(order_id, status):
    order_status[order_id] = status


def get_order_status(order_id):
    return order_status.get(order_id, "not_found")


def get_orders():
    return list(order_queue.queue)
