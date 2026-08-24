import csv
import json

def add_order():
    try:
        
        try:
            file = open("orders.json", "r")
            orders = json.load(file)
            file.close()
        except FileNotFoundError:
            orders = []

        name = input("Enter customer name: ")

        items = input("Enter items: ")
        items = items.split(",")

        amount = float(input("Enter total amount: "))

        status = input("Enter order status: ")

        order = {
            "name": name,
            "items": items,
            "amount": amount,
            "status": status
        }

        orders.append(order)

    
        file = open("orders.json", "w")
        json.dump(orders, file, indent=4)
        file.close()

        print("Order saved!")

    except ValueError:
        print("Please enter a number for amount.")


def view_orders():
    try:
        file = open("orders.json", "r")
        orders = json.load(file)
        file.close()

        print("\n--- All Orders ---")

        for order in orders:
            print("Customer:", order["name"])
            print("Items:", order["items"])
            print("Amount:", order["amount"])
            print("Status:", order["status"])
            print("----------------")

    except FileNotFoundError:
        print("No orders found.")


def export_orders_to_csv():
    try:
        with open("orders.json", "r") as file:
            orders = json.load(file)

        with open("orders.csv", "w", newline="") as file:
            writer = csv.DictWriter(
                file,
                fieldnames=["name", "items", "amount", "status"]
            )
            writer.writeheader()
            for order in orders:
                csv_order = order.copy()
                csv_order["items"] = ", ".join(csv_order["items"])
                writer.writerow(csv_order)

        print("Orders exported to orders.csv!")

    except FileNotFoundError:
        print("No orders found.")


while True:
    print("\n1. Add Order")
    print("2. View Orders")
    print("3. Export orders to CSV")
    print("0. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        add_order()

    elif choice == "2":
        view_orders()

    elif choice == "3":
        export_orders_to_csv()

    elif choice == "0":
        print("Thank you!")
        break

    else:
        print("Wrong choice")