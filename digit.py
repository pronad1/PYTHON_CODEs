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

    if n>=6:
        b=9
    elif n>=3:
        b=3
    else:
        b=1
    if(b*d)%9==0:
        a.append(9)


    print(*a)