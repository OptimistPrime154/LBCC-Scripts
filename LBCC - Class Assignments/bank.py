answer = input("Greeting: ").strip().lower()

if "hello" == answer[0:5]:
    print("$0")
elif "h" == answer[0]:
    print("$20")
else:
    print("$100")