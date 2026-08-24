**Section A: Concept Application — Scenario 2 (S2)**

A dictionary is a much faster and clearer way to store this data than a list of tuples because it allows direct key lookup. For example, we can get the price instantly with `menu['Paneer Burger']`, while a list of tuples would need to search through the items one by one until it finds the right dish.

A big drawback of the list-of-tuples method is that it depends on remembering index positions, like using index `1` for the price. That can easily become confusing and lead to mistakes. Using a dictionary is simpler because each dish name is a unique key, making the code easier to read and helping avoid duplicate entries.