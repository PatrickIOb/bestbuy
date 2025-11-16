class Product:
    """Product class for handling single products directly"""
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
        """returns the quantity of the product"""
        return self.quantity


    def set_quantity(self):
        """sets the quantity of the product"""
        if self.quantity == 0:
            self.active = False


    def is_active(self):
        """checks if the product is active"""
        return self.active


    def activate(self):
        """activates the product"""
        self.active = True


    def deactivate(self):
        """deactivates the product"""
        self.active = False


    def show(self):
        """shows the product"""
        print(f"{self.name}, Price: {self.price}$, Quantity: {self.quantity}")

    def buy(self, quantity):
        """buys the product"""
        if quantity < 0:
            raise ValueError("Quantity cannot be negative")
        elif quantity > self.quantity:
            raise ValueError("Quantity cannot be greater than the product's quantity")
        else:
            self.quantity -= quantity
        return self.price * quantity
