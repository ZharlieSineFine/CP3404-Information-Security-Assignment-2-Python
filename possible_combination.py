import itertools

# Define the possible letters for each position in the keyword
position_options = [
    ['p', 'd', 'y'],  # First letter possibilities
    ['g', 'p', 'b', 'r', 'f'],  # Second letter possibilities
    ['o', 'b', 'y'],  # Third letter possibilities
    ['z', 'd', 'q'],  # Fourth letter possibilities
    ['u', 'i', 'j'],  # Fifth letter possibilities
    ['c', 'r', 'q'],  # Sixth letter possibilities
    ['t', 'p', 'x', 'c', 'i']  # Seventh letter possibilities
]

# Generate all possible combinations of the keyword
keywords = itertools.product(*position_options)

# Initialize a counter
keyword_count = 0

# Convert each combination of letters into a string and print it
for keyword in keywords:
    keyword_str = ''.join(keyword)
    print(keyword_str)
    keyword_count += 1  # Increment the counter with each keyword generated

# Print the total number of keywords generated
print(f"Total number of keywords generated: {keyword_count}")
