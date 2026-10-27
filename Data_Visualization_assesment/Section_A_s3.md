## Section A — Task 3: Choosing Matplotlib Charts

For a monthly report on a food delivery startup, I would use three charts. Each chart helps explain a different part of the business.

1\. Total orders per month — Line chart

A line chart is a good choice for showing how the number of orders changes throughout the year. It makes it easy to see which months had more or fewer orders.

2\. Orders by cuisine type — Pie chart

A pie chart can show how orders are divided between cuisines, such as Fast Food, Indian, Chinese, and Desserts. Each slice represents one cuisine's share of the total orders.

3\. Delivery time distribution — Histogram

A histogram works well for delivery times because they are numbers. It groups the times into ranges and shows how many orders fall in each range. This helps us see the usual delivery time and notice any unusually long deliveries.

Using `plt.subplots()`

We can put all three charts in one figure using `plt.subplots(1, 3)`. This creates one row with three columns, so the charts appear side by side.

I would not use a shared x-axis because each chart shows different information. The line chart uses months, the pie chart shows cuisine types, and the histogram uses delivery-time ranges. Each chart needs its own axis setup.

Overall, I would use a line chart for monthly orders, a pie chart for orders by cuisine, and a histogram for delivery times. Putting them together with `plt.subplots(1, 3)` makes it easy to see all three parts of the report in one figure.