for _ in range(int(input())):
    n,k,x= map(int, input().split())
    a= list(map(int, input().split()))
    suff=[0]*(n+2)
    suff[n]=a[n-1]

    for i in range(n-1,0,-1):
        suff[i]=a[i-1]+suff[i+1]

    s=suff[1]
    ans=0

    for i in range(1,n+1):
        cur=suff[i]
        if cur>=x:
            ans+=k
            continue
        req=x-cur
        if req<=0:
            ans+=k
            continue

        max_available=(k-1)*s

        if req>max_available:
            continue
        t_min=(req+s-1)//s
        i_max=k-t_min

        if i_max<0:
            continue
        ans +=i_max

    print(ans)