
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 1. Generate data
np.random.seed(7)

df = pd.DataFrame({
    'order_value': np.random.uniform(100, 800, 200),
    'distance_km': np.random.uniform(1, 20, 200),
    'delivery_time_mins': np.random.normal(30, 8, 200),
    'rating': np.random.uniform(1, 5, 200),
    'discount_pct': np.random.uniform(0, 30, 200)
})

# 2. Add missing values
for col in ['delivery_time_mins', 'rating']:
    idx = np.random.choice(df.index, 10, replace=False)
    df.loc[idx, col] = np.nan
    df[col] = df[col].fillna(df[col].median())

df['delivery_time_mins'] = df['delivery_time_mins'].clip(lower=1)

# 3. Calculate delivery speed
df['delivery_speed_kmph'] = (
    df['distance_km'] / (df['delivery_time_mins'] / 60)
)

# 4. Create speed categories
df['speed_band'] = pd.qcut(
    df['delivery_speed_kmph'],
    3,
    labels=['Slow', 'Normal', 'Fast']
)

# 5. Correlation heatmap
sns.heatmap(df.select_dtypes('number').corr(),
            annot=True, cmap='coolwarm')
plt.savefig('correlation_heatmap.png', dpi=150,
            bbox_inches='tight')
plt.show()

# 6. Pairplot
sns.pairplot(df, vars=['order_value', 'distance_km',
                       'delivery_time_mins', 'rating'],
             hue='speed_band')
plt.savefig('pairplot.png', dpi=150, bbox_inches='tight')
plt.show()
