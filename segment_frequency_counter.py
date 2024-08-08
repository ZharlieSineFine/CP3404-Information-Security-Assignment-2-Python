from collections import Counter

# Below is the given ciphertext to decrypt
text = """tthxgmekbttwktmxtxxnnxmmxxbmxewntmbxnivbhwvbwtlglagxtnubafxxagmbfuftkmhhmxktgupetnfnxdqgkbkbxlhakxtlbxgkbfthhbbhykhwxlrybxgiwxwlgflkagtgxxxmhxlbm"""

# Remove non-alphabet characters
text = ''.join(filter(str.isalpha, text))

# Count frequency of each letter
frequency = Counter(text)

# Total number of letters
total_letters = sum(frequency.values())

# Sort frequencies by count in descending order
sorted_frequency = sorted(frequency.items(), key=lambda item: item[1], reverse=True)

# Print frequencies as percentages
for letter, count in sorted_frequency:
    percentage = (count / total_letters) * 100
    print(f"{letter}: {count} ({percentage:.2f}%)")
