from collections import defaultdict


def find_repeating_patterns(text, min_length=4):
    # Dictionary to store patterns and their positions using a set to avoid duplicates
    pattern_positions = defaultdict(set)

    # Length of the text
    text_length = len(text)

    # Iterate over all possible lengths of patterns from min_length to half the text length
    for length in range(min_length, text_length // 2 + 1):
        # Use a sliding window to get substrings of current length
        for i in range(text_length - length + 1):
            # Extract the substring
            substring = text[i:i + length]

            # Move the start position ahead and check for further occurrences of this substring
            for j in range(i + length, text_length - length + 1):
                if text[j:j + length] == substring:
                    pattern_positions[substring].add(j)

            # Only consider substrings that appear more than once
            if len(pattern_positions[substring]) > 0:
                # Add the first occurrence position
                pattern_positions[substring].add(i)

    # Filter to keep only those patterns with more than one occurrence and separate first and repeated positions
    final_patterns = {}
    for pattern, positions in pattern_positions.items():
        if len(positions) > 1:
            sorted_positions = sorted(positions)
            first_position = sorted_positions[0]
            repeated_positions = sorted_positions[1:]
            final_patterns[pattern] = (first_position, repeated_positions)

    return final_patterns


def calculate_distances(first_position, repeated_positions):
    return [pos - first_position for pos in repeated_positions]


# Example usage
cryptogram = "pchhlptizjhfatcrifnkhctoqvgxbusvwggszbjchmwvghnvetdsqnrkxtslmdbsuczhttiysunjtcldlhcwjkqkitktmsumgtjthlipmwvghfnxgxfdxwtacmoiyxgjvlmjxgftiytnckwoudnnvfdwexekgdoemxfbvihmwzgwsrxpiszcfxapivyfbcdouegmhnwwbrxgzgkudettcpgqwxkwhmunryovmgtufcgxwmryoxwvbdegkuxxiysquvngrzslqitihbihvdeqhunbcxhkynhhzbjvkwhrzouwvizcqmfbhtivmgwhftdljtkvphyplxeuoykgiysvypltkvdnvatislmqgapcqyuxacsucptrfbwcpndlggiwuavoxwvbdeqguvatisdlgfpemeoaxgjoqxuxacsumyadtcqnkgjfivfamgrrhuubcxzhwqfbfrlnauxugdlgfpkqkyftcuqoycktucyytmxdsdwehguwqavhiysdoemxfbuonxhtrdmcktkmscetacmrjggqzrwbgutjhnhqpcvldgretftdwftxjovyengzhlyufpiyhnunryovnjxcvkbitdhkcfegqryoqaggnjswbgkteczyzbhkbxggkdlgrhnbcvpuimxgjwwyuljtvdmehbdghwvapkcizgkhvfycexhwcunttszbjcplttiucvbtjadlmxijcqfkgtsfregkhvlkcdbikvhmcftwzdquthdcuyehcmsqnkhcrzrhnbcvoxwvbdegdhfhuwsuhqydiarzrkdksfnkhckcecfwtigfixxgruhihlttiucvrxjgxyuydiqguubhcwpcvxsnoqacgscsxhiigfdrmgwpjqkyoxufffipwjthlhilttiuycgsrbrhafdlgfxclwfkhpgkiywvmeatdslmkghvqxlgtcurryugdkogxtxhjhkyuxrlflnkxhdouegmpjdhwvhutrdmyxlzzoxklrlgvnjbhzbvyemxfb"
patterns = find_repeating_patterns(cryptogram)

# Print the patterns, their positions, and distances
for pattern, (first_pos, repeated_pos) in patterns.items():
    distances = calculate_distances(first_pos, repeated_pos)
    print(
        f"Pattern: {pattern}, First Appearing Position: {first_pos}, Repeated Appearing Positions: {repeated_pos}, Distances: {distances}")
