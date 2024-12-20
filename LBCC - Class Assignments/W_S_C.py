import requests
from datetime import datetime

def fetch_bitcoin_data(start_date, end_date):
    # Construct the Coinbase API endpoint URL
    url = "https://api.coinbase.com/v2/prices/BTC-USD/historic?start=" + start_date + "&end=" + end_date
    
    # Make a GET request to the Coinbase API
    response = requests.get(url)
    
    # Check if the request was successful
    if response.status_code == 200:
        return response.json()
    else:
        print("Failed to fetch Bitcoin data:", response.status_code)
        return None

def calculate_investment(start_date, monthly_amount):
    end_date = datetime.now().strftime("%Y-%m-%d")
    bitcoin_data = fetch_bitcoin_data(start_date, end_date)
    
    if bitcoin_data:
        prices = bitcoin_data['prices']
        start_price = prices[0]['price']  # Close price on start date
        end_price = prices[-1]['price']  # Close price on end date
        
        total_months = len(prices)
        total_investment = monthly_amount * total_months
        final_value = end_price * total_months
        
        return final_value - total_investment
    else:
        return None

# User input
start_date = input("Enter start date of investment (YYYY-MM-DD): ")
monthly_amount = float(input("Enter monthly investment amount: "))

# Calculate potential gain/loss
result = calculate_investment(start_date, monthly_amount)
if result is not None:
    if result > 0:
        print(f"You would have gained ${result:.2f}")
    elif result < 0:
        print(f"You would have lost ${abs(result):.2f}")
    else:
        print("You would have broken even")
else:
    print("Calculation failed")