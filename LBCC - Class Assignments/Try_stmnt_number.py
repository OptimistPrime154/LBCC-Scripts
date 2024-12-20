

x = int(input("What is x? "))

print(f"x is {x}")

try:
    x = int(input("What is x? "))
    print(f"x is {x}")
except ValueError:
    print("x is not an interger")
else:
    print(f"x is {x}")

#another way to code this
    
while True:
    try:
        x = int(input("What is x? "))
    except ValueError:
        print("x is not an interger")
    else:
        break

print(f"x is {x}")

# another way more optimal and defensively

def main():
    x = get_int()
    print(f"x is {x}")
def get_int():
    while True:
        try:
            x = int(input("What is x? "))
        except ValueError:
            print("x is not an interger")
        else:
            break
    return x 
main()

#another way

def main():
    x = get_int()
    print(f"x is {x}")

def get_int():
    while True:
        try:
            return int(input("What is x? ")) 
        except ValueError:
            print("x is not an interger")
    
    
main()

import this
