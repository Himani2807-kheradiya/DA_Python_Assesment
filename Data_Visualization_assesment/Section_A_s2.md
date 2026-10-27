**Section A — Task 2: groupby() and agg()**

I would use `groupby()` and `agg()` instead of a for loop because they make it easy to group the data and calculate averages in just a few lines. Using a loop would mean going through each restaurant one at a time, which could make the code longer.

For example, imagine a DataFrame with restaurant names, order values, delivery times, and ratings. I can find the averages for each restaurant like this:

```python
result = df.groupby('restaurant_name').agg({
    'order_value': 'mean',
    'delivery_time_mins': 'mean',
    'rating': 'mean'
})

print(result)
```

`groupby('restaurant_name')` puts the orders for each restaurant together. Then `agg()` applies the calculation to the columns, and `'mean'` finds each average. `print(result)` displays the results.

The resulting DataFrame's index contains the restaurant names. Each row shows that restaurant's average order value, delivery time, and rating.

I find `groupby()` and `agg()` helpful because they let me calculate several averages without writing as much repetitive code.