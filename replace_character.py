def solve():
    n = int(input())
    s = list(input())
    original = s.copy()
    a = [0] * n
    for i in range(n):
        a[i] = s.count(s[i])

    s[a.index(min(a))] = s[a.index(max(a))]
    if s == original:
        for i in range(1, n):
            if s[i] != s[0]:
                s[0] = s[i]
                break
    print(''.join(s))

for _ in range(int(input())):
    solve()


