
for _ in range(int(input())):

    n = int(input())
    a = list(map(int, input().split()))

    freq = [0] * (n + 1)
    b = [0] * n

    for i in range(n):
        ai = a[i]

        freq[ai] += 1
        b[i] = ai

    print(" ".join(map(str, b)))


