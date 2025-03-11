def is_square(l, r, d, u):
    return l == r and d == u and l == d  # All conditions must be met

t = int(input())  # Number of test cases
for _ in range(t):
    l, r, d, u = map(int, input().split())
    print("Yes" if is_square(l, r, d, u) else "No")
