def find_first_repeated_frequency(changes):
    current_frequency = 0
    seen_frequencies = set()
    seen_frequencies.add(current_frequency)  # Initial frequency (0) is added to the set

    while True:
        for change in changes:
            current_frequency += change
            if current_frequency in seen_frequencies:
                return current_frequency
            seen_frequencies.add(current_frequency)

# Test cases
test_cases = [
    [+1, -1],                      # first reaches 0 twice
    [+3, +3, +4, -2, -4],          # first reaches 10 twice
    [-6, +3, +8, +5, -6],          # first reaches 5 twice
    [+7, +7, -2, -7, -4]           # first reaches 14 twice
]

# Apply the function to each test case and print the result
for i, changes in enumerate(test_cases):
    result = find_first_repeated_frequency(changes)
    print(f"Test case {i + 1} first reaches {result} twice.")