# Jhon Patrick Tacio
# Data vis act2 

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import os

current_folder = os.path.dirname(os.path.abspath(__file__))
csv_path = os.path.join(current_folder, "Salesss.csv")

print(f"Looking for file at: {csv_path}")

sns.set_theme(style="whitegrid")

df = pd.read_csv(csv_path)

print("First 5 rows:")
print(df.head())

revenue_by_category = df.groupby("Category")["Revenue"].sum().reset_index()
revenue_by_category = revenue_by_category.sort_values(by="Revenue", ascending=False)

print("\nTotal Revenue:")
print(revenue_by_category)

plt.figure(figsize=(10,6))
sns.barplot(data=revenue_by_category, x="Category", y="Revenue", palette="pastel")
plt.title("Total Revenue per Category - Foods, Clothing, Home & Kitchen, Appliances")
plt.ylabel("Total Revenue ($)")
plt.tight_layout()
plt.savefig(os.path.join(current_folder, "bar_revenue.png"), dpi=300)
plt.show()

pivot_revenue = df.pivot_table(values="Revenue", index="Region", columns="Category", aggfunc="sum", fill_value=0)
print("\nPivoted Table:")
print(pivot_revenue)

plt.figure(figsize=(10,6))
sns.heatmap(pivot_revenue, annot=True, fmt=".0f", cmap="rocket_r", linewidths=1, linecolor="white")
plt.title("Sales Density Heatmap: Region vs Category")
plt.tight_layout()
plt.savefig(os.path.join(current_folder, "heatmap_revenue.png"), dpi=300)
plt.show()