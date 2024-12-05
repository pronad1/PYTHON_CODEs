t = int(input())  # Number of test cases

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))

    total_sum = sum(a)

    # Check if the total sum is divisible by n
    if total_sum % n != 0:
        print("NO")
        continue

    target = total_sum // n  # Target value for each element
    work = 0  # Cumulative "work" required to balance the array
    possible = True

    for i in range(n):
        work += a[i] - target  # Accumulate excess or deficit at this index
        if work < 0:
            possible = False
            break  # Redistribution is not possible

    print("YES" if possible else "NO")
