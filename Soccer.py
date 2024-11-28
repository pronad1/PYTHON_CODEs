for _ in range(int(input())):
    a,b=map(int,input().split())
    x,y=map(int,input().split())

    if a<b and x<y or a>b and x>y:
        print("YES")
    else:
        print("NO")