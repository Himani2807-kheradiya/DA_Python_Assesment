
### Section A — Task 6: Correlation Heatmap

A correlation heatmap is a quick way to see how the dataset’s eight numeric features relate to one another.

```python
correlation = df.corr(numeric_only=True)
sns.heatmap(correlation, annot=True, cmap='coolwarm', vmin=-1, vmax=1)
plt.show()
```

- Colour scale: Correlation values run from -1 to +1. Positive values mean two features tend to increase together, while negative values mean one tends to decrease as the other increases. Values near 0 suggest little linear relationship.
- Reading a cell: For example, a correlation of `0.85` between `distance_km` and `delivery_time_mins` would suggest a strong positive relationship.
- What to look for: I’d take a closer look at correlations with an absolute value of 0.8 or more, since they could point to multicollinearity. This is a useful guideline, not a hard-and-fast rule.

The heatmap can flag highly correlated features before a regression model is trained. Follow-up checks, such as VIF, can help determine whether multicollinearity is a concern.