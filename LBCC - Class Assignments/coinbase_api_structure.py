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

# User input
start_date = input("Enter start date of investment (YYYY-MM-DD): ")
end_date = input("Enter end date of investment (YYYY-MM-DD): ")

# Fetch Bitcoin data
bitcoin_data = fetch_bitcoin_data(start_date, end_date)
if bitcoin_data:
    print(bitcoin_data)
else:
    print("Failed to fetch Bitcoin data")
    