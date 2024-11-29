for _ in range(int(input())):
    n=int(input())
    a=0
    b=0
    for i in range(n):
        x,y=map(int,input().split())
        a=max(a,x)
        b=max(b,y)
    print(2*(a+b))
