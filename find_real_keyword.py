import itertools
import enchant

# Initialize an English dictionary using PyEnchant
dictionary = enchant.Dict("en_US")


def is_likely_english_keyword(keyword):
    """ Check if the keyword contains common English sequences or is a valid word. """
    # Check if the entire keyword is a valid English word
    if dictionary.check(keyword):
        return True
    # Additional checks can include common bi-gram or tri-gram checks
    # For simplicity, this example only checks whole words
    return False


# Define possible letters for each position in the keyword
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
possible_keywords = itertools.product(*position_options)

# Loop through each possible keyword and check if it's likely English
for keyword_tuple in possible_keywords:
    keyword = ''.join(keyword_tuple)
    if is_likely_english_keyword(keyword):
        print(f"Likely English keyword: {keyword}")
