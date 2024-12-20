i = 3
while i != 0:
    print("meow")
    i = i - 1
#^^^^^^Counts down^^^^^^^
i = 1
while i <= 3:
    print("meow")
    i = i + 1
#^^^^^^^Counts up^^^^^^^^
i = 0
while i < 3:
    print("meow")
    i = i + 1 # code to the left is the name as 'i += 1'
# This code also counts up and it is best practice to always start from '0' as a programmer

for i in [0, 1, 2]:
    print("meow")
#cleaner but still not optimal
    
for i in range(3): # range(1000000)
    print("meow")
# this code allows us to choose up to a 1,000,000 without hasving to type 1 through a million

print ("meow\n" * 3, end="")
# code also works an will not give an extra line due to the 'end=""'

while True:
    n = int(input("What's n? "))
    if n < 0:
        continue
    else:
        break
# This code is called a loop
    
while True:
    n = int(input("What's n? "))
    if n > 0:
        break

for _ in range(n):
    print ("meow")
# this code will ask the user for a number and print 'meow' that many times

def main():
    meow(3)

def meow(n):
    for _ in range(n):
        print("meow")


main()
# prints meow 3 times

def main():
    number = get_number()
    meow(number)

def get_number():
    while True:
        n = int(input("What's n? "))
        if n > 0:
           break 
    return n

def meow(n):
    for _ in range(n):
        print("meow")


main()


