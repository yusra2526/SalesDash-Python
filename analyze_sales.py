import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

# Load Data
df = pd.read_csv("sales_data.csv")

# Handle missing values (fill NaN sales with mean value)
df["Sales"].fillna(df["Sales"].mean(), inplace=True)

# Convert Date column to datetime
df["Date"] = pd.to_datetime(df["Date"])

# Display summary
print("Data Summary:\n", df.describe())

# Save cleaned data
df.to_csv("cleaned_sales_data.csv", index=False)

# Grouped Sales by Category
category_sales = df.groupby("Category")["Sales"].sum().reset_index()

# Plotly Interactive Bar Chart
fig = px.bar(category_sales, x="Category", y="Sales", 
             title="Total Sales by Category",
             text_auto=True, color="Sales",
             color_continuous_scale="viridis")

fig.show()
