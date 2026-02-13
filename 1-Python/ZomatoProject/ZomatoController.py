class ZomatoController:
    def __init__(self):
        self.restaurants = []

    def add_restaurant(self, restaurant):
        self.restaurants.append(restaurant)

    def select_restaurant(self, name):
        for restaurant in self.restaurants:
            if restaurant.name.lower() == name.lower():
                if restaurant._is_open:
                    return restaurant
                else:
                    print("Restaurant is currently closed")
                    return None

        print("Restaurant not available")
        return None
