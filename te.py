def winning_index(arr, k):
    n = len(arr)
    remainder_set = set()

    for num in arr:
        remainder = num % k
        if remainder in remainder_set or (k - remainder) in remainder_set:
            continue
        remainder_set.add(remainder)

    if len(remainder_set) == k:
        # If all remainders are present, there's no winning index
        return "NO"

    # Otherwise, any index with a unique remainder is a winning index
    for i in range(n):
        if arr[i] % k in remainder_set:
            return "YES\n" + str(i + 1)


# Read input
t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    arr = list(map(int, input().split()))

    print(winning_index(arr, k))