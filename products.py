class Product:

    def __init__(self, name, price, quantity):

        if name == "":
            raise ValueError("Product name cannot be empty")
        if price < 0:
            raise ValueError("Product price cannot be negative")
        if quantity < 0:
            raise ValueError("Product quantity cannot be negative")

        self.name = name
        self.price = price
        self.quantity = quantity
        self.active = True

    def get_quantity(self):
        return self.quantity


    def set_quantity(self, quantity):
        if self.quantity == 0:
            self.active = False


    def is_active(self):
        if self.active:
            return True
        else:
            return False


    def activate(self):
        self.active = True


    def deactivate(self):
        self.active = False


    def show(self):
        print(f"{self.name}, Price: {self.price}, Quantity: {self.quantity}")

    def buy(self, quantity):
        if quantity < 0:
            raise ValueError("Quantity cannot be negative")
        elif quantity > self.quantity:
            raise ValueError("Quantity cannot be greater than the product's quantity")
        else:
            self.quantity -= quantity
        return self.price * quantity


def main():
    bose = Product("Bose QuietComfort Earbuds", price=250, quantity=500)
    mac = Product("MacBook Air M2", price=1450, quantity=100)

    print(bose.buy(50))
    print(mac.buy(100))
    print(mac.is_active())

    bose.show()
    mac.show()

    bose.set_quantity(1000)
    bose.show()

if __name__ == "__main__":
    main()