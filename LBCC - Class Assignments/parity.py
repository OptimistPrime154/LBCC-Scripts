x = int(input("What is x? "))

if x % 2 == 0:
    print("Even")
else:
    print("Odd")

# version 1

def main():
    x = int(input("What is x? "))
    if is_even (x):
        print("Even")
    else:
        print("Odd")
               
        
def is_even(n):
    if n % 2 == 0:
        return True
    else:
        return False
    
main()

#version 2

def is_even(n):
    return True if n % 2 == 0 else False
      
main ()

#version 3 the pythonic way. approved by the community

def is_even(n):
    return n % 2 == 0 

main()