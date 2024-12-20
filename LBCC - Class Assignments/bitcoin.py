import sys

import requests

import json

if len(sys.argv) != 2:
    print("Missing command-line argument")
    sys.exit(1)

try:
    multiplier = float(sys.argv[1])
except ValueError:
    print("Command-line argument is not a number")
    sys.exit(1)

response = requests.get('https://api.coindesk.com/v1/bpi/currentprice.json')


if response.status_code == 200:
    # Parse the JSON response into a Python dictionary
    data = json.loads(response.text)
    
    # Extract the rate_float for USD
    rate_usd = data['bpi']['USD']['rate_float']
    
    result = rate_usd * multiplier

    print("${:,.2f}".format(result))
