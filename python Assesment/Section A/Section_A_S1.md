******Section A: Concept Application*****

******Scenario 1 (S1)*******

For the four values in the food delivery application, the order total of Rs 499.50 should be stored as a `float` data type because it contains a decimal value amount. The delivery distance of 7.3 km requires a `float` data type because distance is a continuous numeric value with decimal precision. The payment method `'UPI'` should be stored as a `str` (string) data type because it contains text. The restaurant's order-accepting status should be stored as `bool`(Boolean) because it can have either True or False value.


If we mistakenly use an integer (`int`) for Rs 499.50, Python will simply drop the decimal and store it as 499. This causes real problems when we calculate the 10% discount—instead of the correct Rs 49.95, we'd get Rs 49.90 (10% of 499). The final bill ends up being Rs 449.10 instead of Rs 449.55. Over time, these small errors add up and create serious accounting issues in the order processing system.