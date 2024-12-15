def count_pairs(t, test_cases):
    results = []
    for n in test_cases:
        # The number of valid pairs (a, b) is simply n - 1
        results.append(n - 1)
    return results

# Reading input
t = int(input())
test_cases = [int(input()) for _ in range(t)]

# Calculating results
results = count_pairs(t, test_cases)

# Printing results
for result in results:
    print(result)
