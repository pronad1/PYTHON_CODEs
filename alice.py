
t = int(input())
for i in range(t):
    n, a, b = map(int, input().split())
    d,e=0,0

    s =list(input()*2000)
    for i in range(1000):
        if d==a and e==b :print("YES") ; break;
        elif s[i]=='N':e+=1
        elif s[i]=='E':d+=1
        elif s[i]=='S':e-=1
        elif s[i]=='W':d-=1
    else:
        print("NO")