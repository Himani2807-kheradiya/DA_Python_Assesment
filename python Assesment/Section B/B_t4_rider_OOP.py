import csv
import os


class Rider:
    def __init__(self, rider_id, name):
        self.rider_id = rider_id
        self.name = name
        self.status = "Available"
        self.total_deliveries = 0

    def assign_order(self, order_id):
        self.status = "On Delivery"
        print("Order", order_id, "assigned to", self.name)

    def complete_delivery(self):
        self.total_deliveries += 1
        self.status = "Available"
        print("Delivery completed!")

    def display_info(self):
        print("ID:", self.rider_id)
        print("Name:", self.name)
        print("Status:", self.status)
        print("Deliveries:", self.total_deliveries)
        print("----------------")



riders = [
    Rider(1, "Rahul"),
    Rider(2, "Amit"),
    Rider(3, "Raj")
]



if os.path.exists("riders.csv"):
    file = open("riders.csv", "r")
    data = csv.reader(file)

    next(data)

    for row in data:
        for rider in riders:
            if str(rider.rider_id) == row[0]:
                rider.name = row[1]
                rider.status = row[2]
                rider.total_deliveries = int(row[3])

    file.close()



while True:
    print("\n--- Delivery Rider System ---")
    print("1. Show Riders")
    print("2. Assign Order")
    print("3. Complete Delivery")
    print("0. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        for rider in riders:
            rider.display_info()

    elif choice == "2":
        rider_id = int(input("Enter Rider ID: "))
        order_id = input("Enter Order ID: ")

        for rider in riders:
            if rider.rider_id == rider_id:
                rider.assign_order(order_id)

    elif choice == "3":
        rider_id = int(input("Enter Rider ID: "))

        for rider in riders:
            if rider.rider_id == rider_id:
                rider.complete_delivery()

    elif choice == "0":
        file = open("riders.csv", "w", newline="")
        writer = csv.writer(file)

        writer.writerow(["ID", "Name", "Status", "Deliveries"])

        for rider in riders:
            writer.writerow([
                rider.rider_id,
                rider.name,
                rider.status,
                rider.total_deliveries
            ])

        file.close()

        print("Data saved!")
        print("Program ended.")
        break

    else:
        print("Invalid choice!")