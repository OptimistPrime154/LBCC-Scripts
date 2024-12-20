import requests

URL = "https://raw.githubusercontent.com/professor-hillman/lbcc-scripts/main/images/costume1.gif"

response = requests.get(URL)

#print(response.content)

with open("costume1.gif", "wb") as file:
    file.write(response.content)