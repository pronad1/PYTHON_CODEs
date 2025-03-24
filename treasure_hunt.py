for _ in range(int(input())):
    x,y,a=map(int,input().split())
    a+=0.5
    s=x+y
    m=a%s
    if m>x:
        print("YES")
    else:   
        print("NO")
        