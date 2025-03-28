for _ in range(int(input())):
    n,x=map(int,input().split())
    a=map(int,input().split())
    s=sum(a)

    if s==x*n:
        print("YES")
        
    else:
        print("NO")