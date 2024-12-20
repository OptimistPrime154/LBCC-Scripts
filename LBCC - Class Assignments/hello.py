# Gets name from user
name = input ("What's your name? ").strip().title()

first, initial, last = name.split()

# Print personalized welcome to user
print (f"Hello {first} {initial} {last}! A winner is you!")
