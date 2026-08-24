menu = {
    "Pizza": {"price": 200, "category": "Fast Food"},
    "Burger": {"price": 150, "category": "Fast Food"},
    "Pasta": {"price": 180, "category": "Main Course"},
    "Momos": {"price": 100, "category": "Snacks"},
    "Sandwich": {"price": 80, "category": "Snacks"},
    "Juice": {"price": 60, "category": "Drinks"}
}


def view_menu():
    print("\nRestaurant Menu")
    for dish in menu:
        print(dish, "-", menu[dish]["price"], "-", menu[dish]["category"])


def filter_menu():
    category = input("Enter category: ")

    for dish in menu:
        if menu[dish]["category"] == category:
            print(dish, "-", menu[dish]["price"])


def search_menu():
    dish = input("Enter dish name: ")

    if dish in menu:
        print("Price:", menu[dish]["price"])
    else:
        print("Dish not found")


while True:
    print("\n1. View Menu")
    print("2. Filter Category")
    print("3. Search Dish")
    print("0. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        view_menu()

    elif choice == "2":
        filter_menu()

    elif choice == "3":
        search_menu()

    elif choice == "0":
        print("Thank you!")
        break

    else:
        print("Wrong choice")