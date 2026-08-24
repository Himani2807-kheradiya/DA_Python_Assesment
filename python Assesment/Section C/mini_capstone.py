import json
import os


def load_orders():
    try:
        with open("orders.json", "r") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return []


def save_orders(orders):
    with open("orders.json", "w") as file:
        json.dump(orders, file, indent=2)

def place_order(orders):
    name = input("Customer name: ")
    if not name:
        print(" Name cannot be empty")
        return

    items = [item.strip() for item in input("Items (comma separated): ").split(",")]

    try:
        amount = float(input("Total amount: "))
    except ValueError:
        print("Amount must be numeric.")
        return

    order = {
        "order_id": max((o["order_id"] for o in orders), default=0) + 1,
        "customer_name": name,
        "items": items,
        "total_amount": amount,
        "status": "Pending"
    }
    orders.append(order)
    save_orders(orders)
    print("Order placed with ID", order["order_id"])

def view_orders(orders):
    print("\nID | Name | Items | Amount | Status")
    print("------------------------------------")
    for order in orders:
        print(f'{order["order_id"]} | {order["customer_name"]} | '
              f'{len(order["items"])} | {order["total_amount"]} | '
              f'{order["status"]}')

def search_order(orders):
    try:
        oid = int(input("Enter Order ID: "))
    except ValueError:
        print("Invalid ID")
        return

    for order in orders:
        if order["order_id"] == oid:
            print("Found:", order)
            return

    print(" Order not found")

def mark_delivered(orders):
    try:
        oid = int(input("Enter Order ID to mark Delivered: "))
    except ValueError:
        print("Invalid ID")
        return

    for order in orders:
        if order["order_id"] == oid:
            order["status"] = "Delivered"
            save_orders(orders)
            print(" Order marked as Delivered")
            return

    print(" Order not found")


orders = load_orders()

while True:
    print("\n1. Place New Order")
    print("2. View All Orders")
    print("3. Search Order by ID")
    print("4. Mark Order as Delivered")
    print("5. Exit")

    ch = input("Choice: ")

    if ch == "1":
        place_order(orders)
    elif ch == "2":
        view_orders(orders)
    elif ch == "3":
        search_order(orders)
    elif ch == "4":
        mark_delivered(orders)
    elif ch == "5":
        break
    else:
        print(" Invalid choice")
