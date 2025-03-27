for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    counts = {0: 0, 1: 0, 2: 0, 3: 0, 5: 0}
    required = {0: 3, 1: 1, 2: 2, 3: 1, 5: 1}
    found = False
    for i in range(n):
        num = a[i]
        if num in counts:
            counts[num] += 1

        # Check if all required digits are satisfied
        if all(counts[d] >= required[d] for d in required):
            print(i + 1)
            found = True
            break
    if not found:
        print(0)