answer = input("What is the Answer to the Great Question of Life, the Universe, and Everything? ").strip().lower

if answer == "42":
    print("Yes")
elif answer == "Forty Two":
    print("Yes")
elif answer == "forty-two":
    print("Yes")
else:
    print("No")


#other way to do it
 
 match answer:
    case "42" | "forty two" | "forty-two":
        print ("Yes")
    case _:
        print("No")
