for _ in range(int(input())):
    n,x=map(int,input().split())
    a=map(int,input().split())
    s=sum(a)
    av=s//n
    if av==x:
        print("YES")
    else:
        print("NO")