# Order.py
class Order:
    def __init__(self, user, restaurant):
        self.user = user
        self.restaurant = restaurant
        self.items = []

    def add_item(self, item):
        self.items.append(item)

    def show_order(self):
        print(f"\nOrder for {self.user.name} at {self.restaurant.name}:")
        for item in self.items:
            print("-", item)

