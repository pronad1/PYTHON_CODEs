for _ in range(int(input())):
    x=int(input())
    c=0
    a=[0,0,0]
    while min(a)<x:
        c+=1
        a.sort()
        a[0]=a[1]*2+1
    print(c)