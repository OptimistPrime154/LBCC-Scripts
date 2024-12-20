
numbers = [99, 114, 121, 112, 116, 111, 123, 65, 83, 67, 73, 73, 95, 112, 114, 49, 110, 116, 52, 98, 108, 51, 125]

for number in numbers:
    print(chr(number), end="")

#another way
flag = " "
for number in numbers:
    flag += chr(number)
print(flag)
