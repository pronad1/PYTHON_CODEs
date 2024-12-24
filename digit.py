for _ in range(int(input())):
    n,d=map(int,input().split())
    a=[1]
    if n>=3 or d%3==0:
        a.append(3)
    if d==5:
        a.append(5)
    if n>=3 or d==7:
        a.append(7)
    b=0
