import pandas as pd
import matplotlib.pyplot as plt

# Step 1: Load data from CSV
# Replace 'stock.csv' with your file path
df = pd.read_csv('stock.csv')

# Step 2: Convert 'Date' column to datetime type
df['Date'] = pd.to_datetime(df['Date'])

# Step 3: Sort data by Date (just in case)
df = df.sort_values('Date')

# Step 4: Calculate rolling average (7-day window)
df['Rolling_Avg'] = df['Close'].rolling(window=7).mean()
print(df)

# Step 5: Plot closing price and rolling average
plt.figure(figsize=(12,6))
plt.plot(df['Date'], df['Close'], label='Closing Price', color='blue')
plt.plot(df['Date'], df['Rolling_Avg'], label='7-Day Rolling Avg', color='orange')
plt.title('Stock Price Over Time with Rolling Average')
plt.xlabel('Date')
plt.ylabel('Price ($)')
plt.legend()
plt.grid(True)
plt.show()
# Step 6: Save the plot as an image file
plt.savefig('stock_price_plot.png')
print("Plot saved as 'stock_price_plot.png'")
# Note: Ensure that 'stock.csv' contains 'Date' and 'Close' columns