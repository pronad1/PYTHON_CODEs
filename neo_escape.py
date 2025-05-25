for _ in range(int(input())):
    n=int(input())
    a = list(map(int, input().split()))
    ma = max(a)
    pos = a.index(ma)
    c=0
    while ma!=0:
        c+=1
        com=ma
        for i in range(pos+1,n):
            if a[i]>com:
                break
            elif a[i]<com:
                com=a[i]
                a[i] = 0
        for i in range(pos-1,-1,-1):
            if a[i]>com:
                break
            elif a[i]<com:
                com=a[i]
                a[i] = 0
        print(a)
        ma=max(a)

    print(c)