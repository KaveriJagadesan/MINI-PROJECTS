import pandas as pd

# 1. Sample sales dataset
data = {
    'Product': ['A', 'B', 'C', 'A', 'B', 'C', 'A', 'B', 'C'],
    'Region': ['North', 'North', 'North', 'South', 'South', 'South', 'East', 'East', 'East'],
    'Units_Sold': [10, 15, 7, 20, 25, 10, 15, 10, 5],
    'Unit_Price': [100, 150, 200, 100, 150, 200, 100, 150, 200]
}

df = pd.DataFrame(data)

# 2. Calculate total revenue per row
df['Revenue'] = df['Units_Sold'] * df['Unit_Price']

# 3. Find top-selling products by total revenue
top_products = df.groupby('Product')['Revenue'].sum().sort_values(ascending=False)
print("\n--- Top-Selling Products ---")
print(top_products)

# 4. Calculate average revenue per region
avg_revenue_region = df.groupby('Region')['Revenue'].mean()
print("\n--- Average Revenue per Region ---")
print(avg_revenue_region)
