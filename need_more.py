import bisect

t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    if n == 0:
        print(0)
        continue
    dp = [0] * n
    prefix_max = [0] * n
    for i in range(n):
        target = a[i] - 2
        j = bisect.bisect_right(a, target) - 1
        if j >= 0:
            current_dp = prefix_max[j] + 1
        else:
            current_dp = 0
        dp[i] = current_dp
        if i == 0:
            prefix_max[i] = current_dp
        else:
            prefix_max[i] = max(prefix_max[i-1], current_dp)
    print(prefix_max[-1] + 1)

    