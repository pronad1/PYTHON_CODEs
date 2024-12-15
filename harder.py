t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))

    freq = [0] * (n + 1)
    b = [0] * n

    b[n - 1] = n
    freq[n] += 1
    max_freq = 1

    for i in range(n - 2, -1, -1):
        if freq[a[i]] == max_freq:
            b[i] = a[i]
            freq[a[i]] += 1
        else:
            for j in range(1, n + 1):
                if freq[j] < max_freq:
                    b[i] = j
                    freq[j] += 1
                    break
            max_freq += 1

    print(*b)