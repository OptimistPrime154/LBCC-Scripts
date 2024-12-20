# sys module for command line

import sys

print("Hello, my name is", sys.argv[1])
# different way to use sys to prent the index error 
try:
    print("Hello, my name is", sys.argv[1])
except IndexError:
    print("Too few arguments")

if len(sys.argv) < 2:
    print("Too few arguments")
elif len(sys.argv) > 2:
    print("Too many arguments")
else:
    print(f"Hello, my name is {sys.argv[1]}")

if len(sys.argv) < 2:
    sys.exit("Too few arguments")
elif len(sys.argv) > 2:
    sys.exit("Too many arguments")
else:
    sys.exit(f"Hello, my name is {sys.argv[1]}")