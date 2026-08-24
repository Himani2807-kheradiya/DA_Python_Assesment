**Section A: Concept Application — Scenario 3 (S3)**

A regular function defined with `def` works better here because the delivery fee logic has multiple conditions (`if`, `elif`, `else`) across two variables, which makes a lambda expression difficult to read and maintain. Lambda functions are best for quick, simple calculations, so a standard `def` function keeps everything clear and manageable.

Lambda functions shine for straightforward, one-line tasks in this app, like sorting food items by price with `sorted(items, key=lambda x: x['price'])` or calculating a simple 5% tax on an amount.