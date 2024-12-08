def find_interesting_abbreviation(S, T):
    # Set to keep track of characters in T
    set_T = set(T)

    # Find the first common character
    for char in S:
        if char in set_T:
            return char

    # If no common character is found, return -1
    return -1


# Read input
S = input().strip()
T = input().strip()

# Find the interesting abbreviation
result = find_interesting_abbreviation(S, T)

# Print the result
print(result)
