class Order:
    def __init__(self, order_id, product, quantity, status="Pending"):
        self.order_id = order_id
        self.product = product
        self.quantity = quantity
        self.status = status

    def update_status(self, new_status):
        self.status = new_status

    def __str__(self):
        return f"Order ID :{self.order_id},Product:{self.product.name},Quantity:{self.quantity},Status:{self.status}"


class OrderManger:
    def __init__(self):
        self.orders = {}

    def create_order(self, order_id, product, quantity):
        if product.stock >= quantity:
            order = Order(order_id, product, quantity)
            self.orders[order_id] = order
            product.update_stock(-quantity)
            return order
        else:
            return None

    def update_order_status(self, order_id, new_status):
        order = self.get_order(order_id)
        if order:
            order.update_status(new_status)
        return order
