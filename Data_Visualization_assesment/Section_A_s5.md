## Section A — Task 5: Comparing `sns.boxplot()` and `sns.violinplot()`

Both `sns.boxplot()` and `sns.violinplot()` can help compare customer ratings for different types of restaurants. They show the information in different ways.

For this task, I would choose `sns.boxplot()`. The manager wants to compare the ratings and find any unusually high or low ones, and I think a boxplot makes that easier to see.

Here are my reasons:

1. **There are a lot of ratings:** The dataset has 10,000 rows. A boxplot gives a simple summary using the median, quartiles, and whiskers. This makes it easier to compare Fast Food, Fine Dining, and Casual restaurants.

2. **It can show outliers:** Ratings outside the whiskers appear as separate points. These could be unusually high or low ratings, but they are not necessarily errors.

3. **Ratings are whole numbers from 1 to 5:** A violin plot uses a smooth curve, which might make it look like ratings between those numbers are possible. A boxplot seems clearer for this type of rating scale.

**When could a violin plot be useful?**

A violin plot can be useful when we want to look more closely at the shape of the data and see where values are concentrated. This is especially helpful with continuous data. With ratings from 1 to 5, though, its smooth shape can be a little confusing.

**Conclusion:** I would use `sns.boxplot()` for this dataset because it makes the restaurant categories and possible outliers easy to compare. I would use a violin plot if I wanted to explore the shape of the data in more detail.