class User:
    def __init__(self, name):
        self.name = name

    def view_restaurants(self, controller):
        print("\nAvailable Restaurants:")
        for restaurant in controller.restaurants:
            if restaurant._is_open:
                print("-", restaurant.name)

    def choose_restaurant(self, controller, restaurant_name):
        return controller.select_restaurant(restaurant_name)

    def view_menu(self, restaurant):
        print(f"\nMenu at {restaurant.name}:")
        restaurant.show_menu()
