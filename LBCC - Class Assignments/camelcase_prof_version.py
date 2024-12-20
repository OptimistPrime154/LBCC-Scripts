def main():
    var = input("camelCase: ").strip()
    sc = snakecase(var)
    print(sc)

def snakecase(varname):
    newvar = ""
    for letter in varname:
        if letter.isupper():
            newvar += "_" + letter.lower()
        else:
            newvar += letter
    return newvar

main()