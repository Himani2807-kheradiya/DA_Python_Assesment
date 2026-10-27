# Section B - Task 1: Delivery Fee Array Calculator

import numpy as np

np.random.seed(42)
distances = np.random.uniform(1.0, 15.0, 25)

fees = 20 + 5 * distances

print("Delivery Distances (km):")
print(np.round(distances, 2))

print("\nDelivery Fees (Rs):")
print(np.round(fees, 2))

mask = fees > 60

print("\nOrders with delivery fee above Rs 60:")
print("Distances:", np.round(distances[mask], 2))
print("Fees:", np.round(fees[mask], 2))

print("\nDelivery Fee Statistics:")
print("Minimum Fee:", round(np.min(fees), 2))
print("Maximum Fee:", round(np.max(fees), 2))
print("Mean Fee:", round(np.mean(fees), 2))
print("Standard Deviation:", round(np.std(fees), 2))