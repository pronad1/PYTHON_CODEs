for _ in range(int(input())):
    n = int(input())

    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    for i in range(n - 1):
        a[i] = max(0, a[i] - b[i + 1])

    print(sum(a))
