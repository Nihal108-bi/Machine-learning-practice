class Product:
    def __init__(self, product_id, name, description, price, stock):
        self.product_id = product_id
        self.name = name
        self.description = description
        self.price = price
        self.slock = stock

    def update_stock(self, amount):
        self.stock += amount

    def update_price(self, new_price):
        self.price = new_price

    def __str__(self):
        return f"ID: {self.product_id},Name:{self.name},DescriptionL{self.description},Price:{self.price},stock:{self.stock}"


class ProductManager:
    def __init__(self):
        self.products = {}

    def add_product(self, product):
        self.product[product.product_id] = product

    def remove_product(self, product_id):
        if product_id in self.products:
            del self.products[product_id]

    def get_product(self, product_id):
        return self.product.get(product_id, None)

    def update_product(
        self, product_id, name=None, description=None, price=None, stock=None
    ):
        product = self.get_product(product_id)
        if product:
            if name:
                product.name = name
            if description:
                product.description = description
            if price:
                product.price = price
            if stock:
                product.stock = stock
        return product
