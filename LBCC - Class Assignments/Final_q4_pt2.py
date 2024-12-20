#Part 2 Answer: 1158
with open("q4_input.txt") as file:
    depths = [int(line.strip()) for line in file.read().splitlines()]

windows = []

#iterates over depths indices from 0 to length of file minus 3 indexes
for i in range(len(depths) - 2):
    #slicing depths by 3 starting at index 0
    window = depths[i:i+3]
    #sums the sliced elements and appends to windows
    windows.append(sum(window))
#testing
#print(windows)

#counter for sliding window greater than previous
increasing_sums = 0    

#starting range from 1 to compare windows elements
for i in range(1, len(windows)):
    #current sum compared to previous 
    if windows[i] > windows[i - 1]:
        increasing_sums += 1

    

print(f"Part 2 Answer: {increasing_sums}")

