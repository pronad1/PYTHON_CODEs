for i in range(int(input())):
    n=int(input())
    a=list(map(int,input().split()))
    r=n-2
    i=0
    sorted(a)
    for i in range(n-1):
        if r%a[i]==0:
            for j in range(i+1,n):
                if a[i]*a[j]==r:
                    print(a[i],a[j])
                    f=1
                    break

        if f==1:
            break
            
