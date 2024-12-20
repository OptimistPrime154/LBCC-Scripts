# creating dictionary
NATO_dic = {
    "a": "alpha",
    "b": "bravo",
    "c": "charlie",
    "d": "delta",
    "e": "echo",
    "f": "foxtrot",
    "g": "golf",
    "h": "hotel",
    "i": "india",
    "j": "juliett",
    "k": "kilo",
    "l": "lima",
    "m": "mike",
    "n": "november",
    "o": "oscar",
    "p": "papa",
    "q": "quebec",
    "r": "romeo",
    "s": "sierra",
    "t": "tango",
    "u": "uniform",
    "v": "victor",
    "w": "whiskey",
    "x": "xray",
    "y": "yankee",
    "z": "zulu",
    " ": ""
}

# creating input

word = input("Translate: ").strip().lower()


# creating a function that iterates through nato_dic for letter in word
def translated(word):

    translated_word = []

    for letter in word:
        # looking up the phonetic equivalent for each letter
        phonetic_equivalent = NATO_dic.get(
            letter, letter
        )  # if letter not found uses the original letter
        translated_word.append(
            f"{letter} - {phonetic_equivalent}"
        )  # using an f function to add first letter and phonetic equivalent
    return translated_word


# printing each letter with phonetic equivalent using item to iterate through translated word for a list format

for item in translated(word):
    print(item)
