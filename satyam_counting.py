for __ in range(int(input())):
    n = int(input())
    a = []
    ans = 0

    for _ in range(n):
        x,y = map(int, input().split())
        a.append((x, y))
    
    
    c = set(a)

    a.sort()
    
    for i in range(1, n):
        if a[i][0] == a[i - 1][0]:
            ans += n - 2
    for i in c:
        if (i[0] - 1, i[1]^1) in c and (i[0] + 1, i[1]^1) in c:
            ans += 1
    
    print(ans)
