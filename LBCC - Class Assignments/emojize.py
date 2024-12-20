emojis = {":1st_place_medal:": "🥇", ":money_bag:": "💰", ":smile_cat:": "😸",}

user_input = input("Input: ") 

if user_input in emojis:
    
    print("Output: ", emojis[user_input])

else:
    print("404")