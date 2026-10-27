**Section A — Task 1: NumPy Vectorisation**


NumPy vectorisation is usually better than using a Python for loop because it can perform calculations on an entire array at the same time. This makes it faster and cleaner than processing each value one by one in a loop.

For example, if we have 50,000 order distances and the delivery fee is ₹5 per kilometre, NumPy can multiply all the distances by 5 in a single operation.

Broadcasting is what allows NumPy to apply one scalar value, such as 5, to every element in an array without creating a separate array filled with repeated values.

A Python for loop is still useful when each calculation depends on the result of the previous one, such as updating the remaining delivery budget after processing each order.

In conclusion, NumPy vectorisation is faster and more efficient for large numerical calculations, while Python loops are better for tasks that require step-by-step or sequential processing.

Note: Since your assignment asks for Python .py files and screenshots for coding tasks, you only need to submit code and screenshots for questions that specifically require programming. For this conceptual question, a written answer is enough unless your teacher has instructed otherwise.