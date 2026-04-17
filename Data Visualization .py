import pandas as pd # pyright: ignore[reportMissingModuleSource]
import matplotlib.pyplot as plt # pyright: ignore[reportMissingModuleSource]
import seaborn as sns # pyright: ignore[reportMissingModuleSource]

file_path = r"E:\decodelabs Data Science intership\Cleaned_Dataset.xlsx"

try:
    df = pd.read_excel(file_path)
    df['Date'] = pd.to_datetime(df['Date'])
    print("--- Data Loaded for Visualization ---\n")
    sns.set_theme(style="whitegrid")

    plt.figure(figsize=(10, 6))
    product_revenue = df.groupby('Product')['TotalPrice'].sum().sort_values(ascending=False)
    sns.barplot(x=product_revenue.index, y=product_revenue.values, palette="viridis")
    plt.title('Total Revenue by Product', fontsize=15)
    plt.xlabel('Product Name')
    plt.ylabel('Total Revenue ($)')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()
 
    plt.figure(figsize=(12, 6))
    daily_sales = df.groupby(df['Date'].dt.date)['TotalPrice'].sum()
    plt.plot(daily_sales.index, daily_sales.values, marker='o', color='teal', linewidth=2)
    plt.title('Daily Sales Trend', fontsize=15)
    plt.xlabel('Date')
    plt.ylabel('Revenue ($)')
    plt.grid(True, linestyle='--', alpha=0.7)
    plt.tight_layout()
    plt.show()

    plt.figure(figsize=(8, 8))
    payment_counts = df['PaymentMethod'].value_counts()
    plt.pie(payment_counts, labels=payment_counts.index, autopct='%1.1f%%', startangle=140, colors=sns.color_palette("pastel"))
    plt.title('Distribution of Payment Methods', fontsize=15)
    plt.show()
except Exception as e:
    print(f"An error occurred: {e}")