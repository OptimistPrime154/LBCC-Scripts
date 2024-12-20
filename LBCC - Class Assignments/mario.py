print("#")
print("#")
print("#")
#prints 3 #

for _ in range(3):
    print("#")
#does the same shit

def main():
    print_column(3)

def print_column(height):
    for _ in range(height):
        print("#")

main()


def main():
    print_square(3)


def print_square(size):
    #For each row in square
    for i in range(size):
        #For each brick in row
        for j in range(size):
            # Print brick
            print("#", end="")

        print()    

main()
# prints 3 by 3 grid

def main():
    print_square(4)


def print_square(size):
    for i in range(size):
        print("#" * size)
        

main()
#prints 4 by 4 grid using '#'

def main():
    print_square(2)


def print_square(size):
    for i in range(size):
        print_row(size)

def print_row(width):
    print("#" * width)
        

main()