import requests
from datetime import datetime

def fetch_bitcoin_prices(start_date, end_date):
    url = f"https://api.coinbase.com/v2/prices/BTC-USD/spot?start={start_date}T00:00:00Z&end={end_date}T00:00:00Z&granularity=86400"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()['data']
        prices = {datetime.utcfromtimestamp(int(row[0])).strftime('%Y-%m-%d'): float(row[1]) for row in data['prices']}
        return prices
    else:
        print("Failed to fetch Bitcoin prices:", response.status_code)
        return None

def calculate_investment(start_date, end_date, monthly_amount):
    bitcoin_prices = fetch_bitcoin_prices(start_date, end_date)
    if bitcoin_prices:
        total_investment = 0
        for date, price in bitcoin_prices.items():
            total_investment += monthly_amount
        end_price = list(bitcoin_prices.values())[-1]
        total_value = end_price * len(bitcoin_prices)
        return total_value - total_investment
    else:
        return None

# User input
start_date = "2018-10-01"  # Start date of investment
end_date = "2024-04-01"    # End date of investment
monthly_amount = 300        # Monthly investment amount

# Calculate potential gain/loss
result = calculate_investment(start_date, end_date, monthly_amount)
if result is not None:
    if result > 0:
        print(f"You would have gained ${result:.2f}")
    elif result < 0:
        print(f"You would have lost ${abs(result):.2f}")
    else:
        print("You would have broken even")
else:
    print("Calculation failed")