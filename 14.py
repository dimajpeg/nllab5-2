import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Загрузка данных
computer_sales = pd.read_csv("computerSales.csv")
icecream_sales = pd.read_csv("icecreamsales.csv")

# 1. Lollipop диаграмма для Sale Price по Product Type
plt.figure(figsize=(10, 6))
sns.barplot(x="Product Type", y="Sale Price", data=computer_sales, palette="viridis", hue="Product Type")
for index, value in enumerate(computer_sales.groupby('Product Type')['Sale Price'].mean()):
    plt.text(index, value, round(value, 2), color='black', ha="center", va="bottom", fontsize=12)
plt.title("Average Sale Price by Product Type")
plt.xlabel("Product Type")
plt.ylabel("Average Sale Price")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("lollipop_sale_price.png")

# 2. Lollipop диаграмма для Profit по Month
plt.figure(figsize=(10, 6))
profit_by_month = computer_sales.groupby("Month")["Profit"].mean().sort_values()
sns.barplot(x=profit_by_month.index, y=profit_by_month.values, palette="magma", hue=profit_by_month.index)
for index, value in enumerate(profit_by_month.values):
    plt.text(index, value, round(value, 2), color='black', ha="center", va="bottom", fontsize=12)
plt.title("Average Profit by Month")
plt.xlabel("Month")
plt.ylabel("Average Profit")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("lollipop_profit_month.png")

# 3. Lollipop диаграмма для Sales по Temperature (из icecreamsales.csv)
plt.figure(figsize=(10, 6))
sns.barplot(x="Temperature", y="Sales", data=icecream_sales, palette="coolwarm", hue="Temperature")
for index, value in enumerate(icecream_sales["Sales"]):
    plt.text(index, value, value, color='black', ha="center", va="bottom", fontsize=12)
plt.title("Ice Cream Sales by Temperature")
plt.xlabel("Temperature (°F)")
plt.ylabel("Sales")
plt.tight_layout()
plt.savefig("lollipop_sales_temperature.png")

# Отображаем графики
plt.show()
