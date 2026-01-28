from Restaurant import Restaurant
from ZomatoController import ZomatoController
from User import User
from FoodItem import FoodItem
from Order import Order


def main():
    controller = ZomatoController()

    royal = Restaurant("Royal Biryani House", "New Jersey", 4.5)
    kfc = Restaurant("KFC", "Seattle", 2.5)

    royal.open_restaurant()
    kfc.open_restaurant()

    royal.add_item(FoodItem("Chicken Dum Biryani", 14.99))
    royal.add_item(FoodItem("Egg Biryani", 10.99))
    royal.add_item(FoodItem("Chicken 65", 8.99))

    kfc.add_item(FoodItem("Burger", 5.99))
    kfc.add_item(FoodItem("Pizza", 7.99))
    kfc.add_item(FoodItem("Coke", 1.99))

    controller.add_restaurant(royal)
    controller.add_restaurant(kfc)

    user = User("Rahul")

    user.view_restaurants(controller)

    choice = input("\nEnter restaurant name: ")
    selected_restaurant = user.choose_restaurant(controller, choice)

    if not selected_restaurant:
        return

    user.view_menu(selected_restaurant)

    order = Order(user, selected_restaurant)

    print("\nSelect items from the menu (type 'done' to finish):")

    while True:
        choice = input("Enter item name: ")

        if choice.lower() == "done":
            break

        item_found = False

        for food in selected_restaurant.menu:
            if food.name.lower() == choice.lower():
                order.add_item(food)
                print(f"{food.name} added to order")
                item_found = True
                break

        if not item_found:
            print("❌ Item not available in this restaurant")

    order.show_order()


if __name__ == "__main__":
    main()