print("===== FOOD DELIVERY BILL CALCULATOR =====")

n = int(input("Enter number of food items: "))

items = []
subtotal = 0

for i in range(n):
    name = input("Enter food item: ")
    price = float(input("Enter price: "))

    if price < 0:
        print("Price cannot be negative!")
        exit()

    items.append((name, price))
    subtotal = subtotal + price


try:
    orders = int(input("Enter number of previous orders: "))

    if orders < 0:
        print("Order count cannot be negative!")
        exit()

except ValueError:
    print("Invalid order count! Please enter a number.")
    exit()


gst = subtotal * 0.18

delivery_fee = 30

discount = 0

if orders > 5:
    discount = subtotal * 0.10


final_amount = subtotal + gst + delivery_fee - discount


print("\n========== RECEIPT ==========")

for name, price in items:
    print(name, ":", "₹", format(price, ".2f"))

print("-----------------------------")
print("Subtotal       : ₹", format(subtotal, ".2f"))
print("GST (18%)      : ₹", format(gst, ".2f"))
print("Delivery Fee   : ₹", format(delivery_fee, ".2f"))

if discount > 0:
    print("Discount (10%) : -₹", format(discount, ".2f"))

print("-----------------------------")
print("Final Amount   : ₹", format(final_amount, ".2f"))
print("=============================")