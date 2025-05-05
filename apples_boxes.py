def apples_in_boxes(test_cases):
    results = []
    for n, k, a in test_cases:
        min_a = min(a)
        limit = min_a + k
        total = sum(min(ai, limit) for ai in a)
        if total % 2 == 1:
            results.append("Tom")
        else:
            results.append("Jerry")
    return results

# Input reading
t = int(input())
test_cases = []
for _ in range(t):
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    test_cases.append((n, k, a))

# Solve and print results
results = apples_in_boxes(test_cases)
for res in results:
    print(res)
