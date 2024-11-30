for _ in range(int(input())):
    m,n = map(int, input().split())
    a=max(m,n)
    b=min(m,n)
    r=a
    while r%b!=0:
        r+=a
    print(r)