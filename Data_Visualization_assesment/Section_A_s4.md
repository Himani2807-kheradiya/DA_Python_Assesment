**Section A — Task 4: Using `plt.annotate()`**


The `plt.annotate()` function helps us point out an important spot on a chart. It adds a label and an arrow so it’s clear where to look.

First, we use `np.argmax()` to find the day with the highest order volume in our 90-day data. Then, we use `plt.annotate()` to show the day number and order volume near the peak, with an arrow pointing to it.

The main parameters are:
1. `xy` — The coordinates of the peak where the arrow points.
2. `xytext` — Where the label appears.
3. `arrowprops` — Controls the arrow’s appearance, such as its style and colour.

This makes the busiest day easy to spot without having to search through the chart.