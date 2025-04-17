for _ in range(int(input())):
    n,m,l,r=map(int,input().split())
    x=abs(l)
    d=n-m
    if x>=d:
        x-=d
        d=0
    else:
        d-=x
        x=0

    print(-x,"",r-d)