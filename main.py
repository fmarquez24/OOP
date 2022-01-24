class Item:
    pay_rate = 0.8 # the pay rate after 20 % discount

    def __init__(self, name: str, price: float, quantity=0):
        # Run validations to the received arguments
        assert price >= 0, f"Price {price} is not greater than or equal to zero!"
        assert quantity >= 0, f"Price {price} is not greater than or equal to zero!"

        # Assign to self object
        self.name = name
        self.price = price
        self.quantity = quantity

    def calculate_total_price(self):
        return self.price * self.quantity


item1 = Item("phone", 100, 1)
item2 = Item("Laptop", 1000, 3)

print(Item.__dict__) # all the attributes for Class Level
print(item1.__dict__) # All the attributes for Instance Level.

