t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    
    
    reversed_a = a[::-1]
    prefix_sum_rev = [0] * (n + 1)
    for i in range(1, n+1):
        prefix_sum_rev[i] = prefix_sum_rev[i-1] + reversed_a[i-1]

    prefix_max = [0] * (n + 1)
    if n >= 1:
        current_max = a[0]
        prefix_max[1] = current_max
        for i in range(2, n+1):
            current_max = max(current_max, a[i-1])
            prefix_max[i] = current_max
    result = []
    for k in range(1, n+1):
        m = n - k + 1
        sum_k = prefix_sum_rev[k-1] + prefix_max[m]
        result.append(str(sum_k))
    print(' '.join(result), end=' \n')
        