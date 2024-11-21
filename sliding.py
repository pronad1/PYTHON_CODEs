for _ in range(int(input())):
    n,m,r,c=map(int,input().split())
    x=m*(n-r) + n*m-((r-1)*m+c) - (n-r)
    print(x)