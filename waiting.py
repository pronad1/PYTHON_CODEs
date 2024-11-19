
b=1
for _ in range(int(input())):
    x,n=input().split()
    n=int(n)
    if x=='P':
        b+=n
    else:
        if b<=n:
            print("YES")
            b=1
        else:
            print("NO")
            b-=n
    