import requests

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

def extract_prices(bitcoin_data):
    if 'data' in bitcoin_data and 'prices' in bitcoin_data['data']:
        return bitcoin_data['data']['prices']
    else:
        print("No price data available")
        return None

def calculate_investment(prices, monthly_amount):
    total_investment = monthly_amount * len(prices)
    final_value = float(prices[-1]['price'])
    return final_value - total_investment, total_investment

# User input
start_date = input("Enter start date of investment (YYYY-MM-DD): ")
end_date = input("Enter end date of investment (YYYY-MM-DD): ")
monthly_amount = float(input("Enter monthly investment amount: "))

# Fetch Bitcoin data
bitcoin_data = fetch_bitcoin_data(start_date, end_date)
if bitcoin_data:
    prices = extract_prices(bitcoin_data)
    if prices:
        gain_loss_total, total_investment = calculate_investment(prices, monthly_amount)
        if gain_loss_total is not None:
            gain_loss_per_month = gain_loss_total / (len(prices) - 1)
            if gain_loss_total > 0:
                print(f"You would have gained ${gain_loss_total:.2f} in total")
            elif gain_loss_total < 0:
                print(f"You would have lost ${abs(gain_loss_total):.2f} in total")
            else:
                print("You would have broken even")
                
            print(f"Average gain/loss per month: ${gain_loss_per_month:.2f}")
            print(f"Total investment: ${total_investment:.2f}")
        else:
            print("Calculation failed")
else:
    print("Failed to fetch Bitcoin data")