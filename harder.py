t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))

    b = [0] * n
    freq = [0] * (n + 1)

    for i in range(n):
        b[i] = a[i]
        freq[b[i]] += 1


    print(" ".join(map(str, b)))
