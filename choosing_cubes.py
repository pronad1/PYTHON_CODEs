for _ in range(int(input())):
    n,f,k = map(int,input().split())
    f-=1
    k-=1
    a=list(map(int,input().split()))
    x=a[f]
    a.sort(reverse=True)
    if a[k] > x:
        print("NO")
    elif a[k] < x:
        print("YES")
    else:
        print("YES" if k==n-1 or a[k+1]<x else "MAYBE")