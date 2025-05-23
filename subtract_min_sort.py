for _ in range(int(input())):
    n= int(input())
    a = list(map(int, input().split()))

    f=1
    for i in range(n-1):
        x=min(a[i],a[i+1])
        a[i]=a[i]-x
        a[i+1]=a[i+1]-x
        if a[i]>a[i+1]:
            print("NO")
            f=0
            break

    if f:
        print("YES")