#Part 1 Answer:1184
with open("q4_input.txt") as file:
    depths = [int(line.strip()) for line in file.read().splitlines()]
    #Testing
    #print(depths)

#Have to figure out number of increases
increases = 0
#iterating through the list strating from the second index
for i in range(1, len(depths)):
    #comparing depths at index levels. If index is more that previous increase plus 1
    if depths[i] > depths[i - 1]:
        increases += 1
#test
#print(increases)
print(f"Part 1 Answer:{increases}")