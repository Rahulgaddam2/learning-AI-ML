class Restaurant:
    def __init__(self, name, location, rating):
        self.name = name
        self.location = location
        self.rating = rating
        self._is_open = False
        self.menu = []

    def open_restaurant(self):
        self._is_open = True

    def close_restaurant(self):
        self._is_open = False

    def add_item(self, food_item):
        self.menu.append(food_item)

    def show_menu(self):
        for item in self.menu:
            print(item)
    
