for _ in range(int(input())):
    n,f,k = map(int,input().split())
    f-=1
    k-=1
    a=list(map(int,input().split()))
    x=a[f]
    a.sort(reverse=True)
