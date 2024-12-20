#names = []

#for _ in range(3):
#    names.append(input("What os your name? "))

#for name in sorted(names):
#    print(f"Hello {name}!")

#name = input("What is your name?" )

#file = open("names.txt", "a")
#file.write(f"{name}\n")
#file.close()

#name = input("What is your name?" )

#with open("names.txt", "a") as file:
#    file.write(name + "\n")

#with open("names.txt", "r") as file:
#    content = file.readlines()

#for line in file:
#    print("Hello", line.rstrip())

#print(content)
######################################################
#with open("names.txt", "r") as file:
#    for line in file:
#        print("Hello", line.rstrip())
#print()

#names = []

#with open("names.txt", "r") as file:
#    for line in file:
#        names.append(line.rstrip())

#for name in sorted(names):
#    print("Hello", name)
wordlist = ["apple", "banana", "cherry", "date", "elderberry", "fig", "grape", "honeydew", "kiwi", "lemon"]

for word1 in wordlist:
    for word2 in wordlist:
        print(word1 + "-" + word2)


