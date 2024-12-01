for _ in range(int(input())):
    n,m,k=map(int,input().split())
    s=str(input())
    x=0
    y=0
    z=0
    while z<n:
        if s[z]=='0':
            y+=1
        else:
            y=0


        if y==m:
            x+=1
            y=0
            z+=k-1

        z+=1

    print(x)


