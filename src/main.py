import yfinance as yf
import pandas as pd

tickers = ['AAPL', 'MSFT', 'GOOGL']
data = {}
for ticker in tickers:
    stock = yf.Ticker(ticker)
    hist = stock.history(period="1mo")
    data[ticker] = hist

# Combine data into a single DataFrame
combined_data = pd.concat(data, axis=1)
print(combined_data).to_csv('stock_data.csv')

print("Stock data saved to stock_data.csv")

combined_data.to_csv('stock_data.csv')  
print("Stock data saved to stock_data.csv")


