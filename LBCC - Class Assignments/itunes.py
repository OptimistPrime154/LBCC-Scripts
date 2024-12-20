import sys

import json

import requests


if len(sys.argv) != 2:
    sys.exit()

response = requests.get("https://itunes.apple.com/search?entity=song&limit=20&term=" + sys.argv[1])

obj = response.json()

for result in obj["results"]:
    print(result["trackName"])