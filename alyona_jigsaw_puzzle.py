for _ in range(int(input())):
    n=int(input())
    arr=list(map(int,input().split()))
    c=1
    s=-1
    d=8
    for i in range(n):
        s+=arr[i]
        if int(s/d)>=1:
            c+=1
            d+=
