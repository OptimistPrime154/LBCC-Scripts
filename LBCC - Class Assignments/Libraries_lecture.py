import random

coin = random.choice(["heads", "tails"])
print(coin)

# This way calls just choice from the random library
from random import randint

number = randint(1, 10)
print(number)

from random import shuffle

cards = ["jack", "queen", "king", "ace"]
shuffle(cards)


for card in cards:
    print(card)