for _ in range(int(input())):
    n,k= map(int, input().split())
    a = list(map(int, input().split()))
    a.sort()
    c,l,r= 0,0,n-1
    while l<r:
        if k==a[l]+a[r]:
            c+=1
            l+=1
            r-=1
        elif k<a[l]+a[r]:
            r-=1    
        else:
            l+=1
    print(c)