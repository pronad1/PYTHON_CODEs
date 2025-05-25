for _ in range(int(input())):
    n=int(input())
    a = list(map(int, input().split()))
    ma = max(a)
    pos = a.index(ma)
    c=0
    if pos==0:
        for i in range(1, n):
            if a[i]<ma:
                ma= a[i]
            elif a[i] > ma:
                c += 1
                ma = a[i]
        if a[n-1]>a[n-2]:
            c += 1
    elif pos == n-1:
        for i in range(n-2, -1, -1):
            if a[i]<ma:
                ma= a[i]
            elif a[i] > ma:
                c += 1
                ma = a[i]
        if a[0]>a[1]:
            c += 1
    else:
        c=1
        for i in range(pos-1, -1, -1):
            if a[i]<ma:
                ma= a[i]
            elif a[i] > ma:
                c += 1
                ma = a[i]
        for i in range(pos+1, n):
            if a[i]<ma:
                ma= a[i]
            elif a[i] > ma:
                c += 1
                ma = a[i]
        if a[0]>a[1]:
            c += 1
        if a[n-1]>a[n-2]:
            c += 1


    print(c)