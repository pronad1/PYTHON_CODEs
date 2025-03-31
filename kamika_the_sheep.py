for _ in range(int(input())):
    n=int(input())
    a=list(map(int,input().split()))

    x=max(a)
    y=min(a)
    z=x-y
    print(z)