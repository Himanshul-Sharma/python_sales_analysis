import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Create a sample sales dataset
data = {
    "Product": ["Laptop", "Mobile", "Tablet", "Laptop", "Mobile",
                "Tablet", "Laptop", "Mobile", "Tablet", "Laptop"],
    "Category": ["Electronics"] * 10,
    "Quantity": [2, 5, 3, 1, 4, 6, 2, 3, 4, 1],
    "Price": [50000, 15000, 20000, 50000, 15000,
              20000, 50000, 15000, 20000, 50000],
    "City": ["Delhi", "Mumbai", "Chandigarh", "Delhi", "Mumbai",
             "Chandigarh", "Delhi", "Mumbai", "Chandigarh", "Delhi"]
}

df = pd.DataFrame(data)

# Calculate sales revenue
df["Sales"] = df["Quantity"] * df["Price"]

# Display the dataset
print("SALES DATASET")
print(df)

print("\nTOTAL SALES:", df["Sales"].sum())
print("TOTAL QUANTITY SOLD:", df["Quantity"].sum())
print("AVERAGE SALE VALUE:", round(df["Sales"].mean(), 2))
# Product-wise sales analysis
print("\nPRODUCT-WISE REVENUE")
product_sales = df.groupby("Product")["Sales"].sum().sort_values(ascending=False)
print(product_sales)

# City-wise sales analysis
print("\nCITY-WISE REVENUE")
city_sales = df.groupby("City")["Sales"].sum().sort_values(ascending=False)
print(city_sales)

# Best-performing product and city
print("\nBEST-SELLING PRODUCT:", product_sales.idxmax())
print("HIGHEST-REVENUE CITY:", city_sales.idxmax())

# -----------------------------------
# DATA VISUALIZATION
# -----------------------------------

# 1. Product-wise revenue chart
plt.figure(figsize=(8, 5))
product_sales.plot(kind="bar")
plt.title("Product-wise Revenue Analysis")
plt.xlabel("Product")
plt.ylabel("Revenue (INR)")
plt.xticks(rotation=0)
plt.tight_layout()
plt.savefig("product_sales.png")
plt.show()

# 2. City-wise revenue chart
plt.figure(figsize=(8, 5))
city_sales.plot(kind="bar")
plt.title("City-wise Revenue Analysis")
plt.xlabel("City")
plt.ylabel("Revenue (INR)")
plt.xticks(rotation=0)
plt.tight_layout()
plt.savefig("city_sales.png")
plt.show()

# 3. Sales distribution by product
plt.figure(figsize=(7, 7))
plt.pie(
    product_sales.values,
    labels=product_sales.index,
    autopct="%1.1f%%",
    startangle=90
)
plt.title("Revenue Share by Product")
plt.tight_layout()
plt.savefig("revenue_share.png")
plt.show()

print("\nCharts created and saved successfully!")

# -----------------------------------
# EXPORT ANALYSIS RESULTS
# -----------------------------------

# Save the cleaned sales dataset
df.to_csv("sales_analysis_results.csv", index=False)

# Save product-wise revenue
product_sales.to_csv("product_revenue.csv", header=["Revenue"])

# Save city-wise revenue
city_sales.to_csv("city_revenue.csv", header=["Revenue"])

print("\nAll analysis files exported successfully!")

