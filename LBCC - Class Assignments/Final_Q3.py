#Part 1 Answer: 472

#open file

with open("q3_input.txt") as file:
    frequencies = file.read().splitlines()

    #testing
    #print(frequencies)

#Start
frequency = 0
#iterating through list
for number in frequencies:
    frequency += int(number) #all numbers added and subtracted

print(f"Part 1 Answer: {frequency}")