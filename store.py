import products
from products import Product


class Store:

    def __init__(self, products):
        # list of Product objects
        self.products = list(products)

    def add_product(self, product):
        self.products.append(product)

    def remove_product(self, product):
        self.products.remove(product)

    def get_total_quantity(self):
        total = 0
        for product in self.products:
            total += product.get_quantity()
        return total

    def get_all_products(self):
        # return only active products
        return [prod for prod in self.products if prod.is_active()]

    def order(self, shopping_list) -> float:
        """
        shopping_list is a list of tuples: (Product, quantity)
        Buy each product, sum up total price
        """
        total_price = 0

        # First validate the entire order BEFORE buying anything
        for product, quantity in shopping_list:
            if quantity > product.get_quantity():
                raise ValueError(
                    f"Not enough quantity for {product.name}"
                )

        # If all good, perform the buys
        for product, quantity in shopping_list:
            total_price += product.buy(quantity)

        return total_price

