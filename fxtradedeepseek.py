import requests
import pandas as pd

# Replace with your API key
API_KEY = 'fff5dcb1540bc04ad848a961'
BASE_URL = f'https://v6.exchangerate-api.com/v6/fff5dcb1540bc04ad848a961/pair/USD/EUR'

def get_exchange_rates(base_currency):
    url = f'https://v6.exchangerate-api.com/v6/{API_KEY}/latest/{base_currency}'
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return data['conversion_rates']
    else:
        print("Failed to fetch data")
        return None

# Example: Fetch exchange rates for USD as base currency
exchange_rates = get_exchange_rates('USD')
if exchange_rates:
    print(exchange_rates)
    
import numpy as np
import matplotlib.pyplot as plt

# Simulate historical exchange rate data (for demonstration)
dates = pd.date_range('2023-01-01', periods=100, freq='D')
rates = np.random.normal(1.0, 0.02, 100).cumsum()  # Simulated exchange rates

# Create a DataFrame
data = pd.DataFrame({'Date': dates, 'ExchangeRate': rates})
data.set_index('Date', inplace=True)

# Calculate moving averages
data['Short_MA'] = data['ExchangeRate'].rolling(window=10).mean()
data['Long_MA'] = data['ExchangeRate'].rolling(window=50).mean()

# Generate trading signals
data['Signal'] = 0
data['Signal'][10:] = np.where(data['Short_MA'][10:] > data['Long_MA'][10:], 1, -1)
data['Position'] = data['Signal'].diff()

# Plot the data
plt.figure(figsize=(12, 6))
plt.plot(data['ExchangeRate'], label='Exchange Rate')
plt.plot(data['Short_MA'], label='10-Day MA')
plt.plot(data['Long_MA'], label='50-Day MA')
plt.plot(data[data['Position'] == 1].index, data['Short_MA'][data['Position'] == 1], '^', markersize=10, color='g', lw=0, label='Buy Signal')
plt.plot(data[data['Position'] == -1].index, data['Short_MA'][data['Position'] == -1], 'v', markersize=10, color='r', lw=0, label='Sell Signal')
plt.legend()
plt.title('FX Trading Strategy - Moving Average Crossover')
plt.show()    

# Calculate daily returns
data['Daily_Return'] = data['ExchangeRate'].pct_change()

# Calculate strategy returns
data['Strategy_Return'] = data['Daily_Return'] * data['Signal'].shift(1)

# Calculate cumulative returns
data['Cumulative_Market_Return'] = (1 + data['Daily_Return']).cumprod()
data['Cumulative_Strategy_Return'] = (1 + data['Strategy_Return']).cumprod()

# Plot cumulative returns
plt.figure(figsize=(12, 6))
plt.plot(data['Cumulative_Market_Return'], label='Market Return')
plt.plot(data['Cumulative_Strategy_Return'], label='Strategy Return')
plt.legend()
plt.title('Cumulative Returns - Market vs Strategy')
plt.show()
