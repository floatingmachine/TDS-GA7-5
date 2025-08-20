---

## 🐍 chart.py  

```python
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# -----------------------------
# 1. Generate synthetic data
# -----------------------------
np.random.seed(42)

products = ["Product A", "Product B", "Product C", "Product D", "Product E"]
regions = ["North", "South", "East", "West"]

data = []
for product in products:
    for region in regions:
        sales = np.random.randint(50, 200)  # simulate sales units
        data.append([product, region, sales])

df = pd.DataFrame(data, columns=["Product", "Region", "Sales"])

# -----------------------------
# 2. Seaborn Styling
# -----------------------------
sns.set_style("whitegrid")
sns.set_context("talk")

# -----------------------------
# 3. Create the barplot
# -----------------------------
plt.figure(figsize=(8, 8))  # 8x8 inches → 512x512 px at dpi=64

ax = sns.barplot(
    x="Product",
    y="Sales",
    hue="Region",
    data=df,
    palette="Set2",
    errorbar=None
)

# -----------------------------
# 4. Chart Customization
# -----------------------------
ax.set_title("Quarterly Product Sales by Region", fontsize=16, weight="bold")
ax.set_xlabel("Product", fontsize=12)
ax.set_ylabel("Sales Units", fontsize=12)

# Add legend with title
plt.legend(title="Region", bbox_to_anchor=(1.05, 1), loc='upper left')

# -----------------------------
# 5. Save the figure
# -----------------------------
plt.tight_layout()
plt.savefig("chart.png", dpi=64, bbox_inches="tight")
plt.close()
