#Part 2 Answer: 66932

#open file
#stripping, reading contents, splitting, intergering???
with open("q3_input.txt") as file:
    frequencies = [int(line.strip()) for line in file.read().splitlines()] 
    #testing
    #print(frequencies)

#Start
current_frequency = 0
#All frequencies
seen_frequencies = set()
# adding (0) to the set
seen_frequencies.add(current_frequency)
#If found_frequency found then it can be True to break
found_frequency= False

#using not to process loop until found
while not found_frequency:
    #iterating
    for change in frequencies:
        #updating frequency
        current_frequency += change
        #checking to see if current frequency has been encountered
        if current_frequency in seen_frequencies:
            found_frequency = True
            break
        #adds current_frequency to seen_frequencies
        seen_frequencies.add(current_frequency)
        
print(f"Part 2 Answer: {current_frequency}")