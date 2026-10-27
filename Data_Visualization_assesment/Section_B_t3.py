
import numpy as np
import matplotlib.pyplot as plt  # type: ignore[reportMissingModuleSource]
np.random.seed(42)

months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun',
          'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']

orders = np.random.randint(1000, 5001, 12)
revenue = orders * np.random.uniform(200, 400, 12)
delivery = np.random.normal(28, 4, 500)

fig, ax = plt.subplots(1, 3, figsize=(16, 5))

ax[0].plot(months, orders, marker='o')
for i, v in enumerate(orders):
    ax[0].annotate(str(v), (i, v), xytext=(0, 5),
                   textcoords='offset points', ha='center')
ax[0].set(title='Monthly Orders', xlabel='Month',
          ylabel='Total Orders')
ax[0].tick_params(axis='x', rotation=45)

colors = ['green' if v > 800000 else 'red' for v in revenue]
ax[1].bar(months, revenue, color=colors)
ax[1].axhline(800000, color='black', linestyle='--')
ax[1].set(title='Monthly Revenue', xlabel='Month', ylabel='Revenue (Rs)')
ax[1].tick_params(axis='x', rotation=45)

# 3. Delivery time histogram
ax[2].hist(delivery, bins=15, edgecolor='black')
ax[2].axvline(np.mean(delivery), color='red',
              linestyle='--', label='Mean')
ax[2].set(title='Delivery Time', xlabel='Minutes',
          ylabel='Frequency')
ax[2].legend()

fig.suptitle('Food Delivery Dashboard')
fig.tight_layout(rect=[0, 0, 1, 0.92])
plt.savefig('food_delivery_dashboard.png', dpi=150)
plt.show()
