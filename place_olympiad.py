t = int(input())
for _ in range(t):
    n, m, k = map(int, input().split())

    if k == 0:
        print(0)
        continue

    low, high, ans = 1, m, m

    while low <= high:
        mid = (low + high) // 2
        case1 = (m + 1) // 2
        case2 = (mid * (m + 1)) // (mid + 1)
        max_per_row = max(case1, min(case2, m))
        total = max_per_row * n

        if total >= k:
            ans = mid
            high = mid - 1
        else:
            low = mid + 1

    print(ans)
