t = int(input())
for _ in range(t):
    n, x = map(int, input().split())
    result = list(range(x)) + list(range(n - 1, x - 1, -1))
    print(' '.join(map(str, result)))
