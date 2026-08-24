
**Section A: Delivery tracking System— Scenario 5 (S5)**

A class is a better choice than using separate variables or a simple dictionary because it keeps the rider’s information and related actions together in one organized, reusable object. This makes the code easier to understand and maintain than having the data and functions separated.

The first OOP principle used is encapsulation. It keeps delivery details, such as GPS coordinates and order status, together with the methods that update them, such as changing the rider’s location or marking an order as complete. This helps ensure that the data is changed safely and consistently. The second principle is abstraction. It hides the more complicated details, such as validating coordinates and managing status changes, while providing simple methods like `complete_delivery()` for the rest of the application to use.