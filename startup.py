for _ in range(int(input())):
    n,k=map(int,input().split())
    arr=[0]*k
    for i in range(k):
        a,b=map(int,input().split())
        arr[a-1] +=b
    c=sorted(arr,reverse=True)
    r=0
    for i in range(min(n,k)):
        r+=c[i]
    print(r)