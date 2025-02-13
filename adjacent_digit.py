for i in range(int(input())):
    x,y=map(int,input().split())
    if x+1>=y and (x+1-y)%9==0:
        print("YES")
    else:   
        print("NO")