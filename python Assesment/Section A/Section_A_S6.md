**Section A : delivery Cost Calculater - Senario-6 (S6)**


When a user enters text instead of a numeric value, Python is unable to convert the string and raises a **ValueError**.

To handle this gracefully without terminating the program, the input and type-conversion statements should be placed inside an infinite `while` loop. Inside this loop, the conversion operation is enclosed in a `try` block followed by a `break` statement to exit the loop once valid numeric input is provided. The corresponding `except ValueError` block catches the invalid input, prints a clear error message instructing the user to enter a numeric value, and allows the loop to iterate so the user is immediately prompted again.