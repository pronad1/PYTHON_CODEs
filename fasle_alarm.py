for _ in range(int(input())):
    n, x = map(int, input().split())
    a = list(map(int, input().split()))

    l = a.index(1)

    a_rev = list(reversed(a))
    
    r = a_rev.index(1)
    r = n - r
    
    tot=r-l

    if tot <= x:
        print("YES")
    else:
        print("NO")