import requests
import pandas as pd

# API configuration
API_URL = 'https://v6.exchangerate-api.com/v6/fff5dcb1540bc04ad848a961/pair/USD/EUR'  # Replace with your API URL
API_KEY = "fff5dcb1540bc04ad848a961"  # Add your API key if required (some APIs need authentication)

# Fetch exchange rate data
response = requests.get(API_URL)
if response.status_code == 200:
    data = response.json()
    print(data)
    rates = data.get("conversion_rate", {})
    print(rates)
    base_currency = data.get("base_code", "USD")
    print(base_currency)
    target_currency =data.get("target_code", "EUR")
    print(target_currency)   
    date = data.get("time_last_update_utc", "Unknown")

    # Convert rates dictionary to DataFrame
    df = pd.DataFrame(
        [{
    "Base Currency" : base_currency,
    "Target_currency" : target_currency,
    "Exchange Rate": rates,
    "Last Updated" : date
    }]
    )
    
    print(df)

    # Save to Excel
    output_file = "exchange_rates1.xlsx"
    df.to_excel(output_file, index=False)

    print(f"Exchange rate data has been saved to '{output_file}'.")
else:
    print(f"Failed to fetch data. Status code: {response.status_code}")


# import requests


# # Where USD is the base currency you want to use
# url = 'https://v6.exchangerate-api.com/v6/fff5dcb1540bc04ad848a961/pair/USD/EUR'

# # Making our request
# response = requests.get(url)
# data = response.json()

# # Your JSON object
# print (data)