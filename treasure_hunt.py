for _ in range(int(input())):
    x,y,a=map(int,input().split())
    d=a*5
    s=x+y
    m=d%s
    if m==0:
        print("YEs")
    else:
        if m>x:
            print("YES")
        else:   
            print("NO")