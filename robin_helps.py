for _ in range(int(input())):
    n,k = map(int,input().split())
    r=0
    c=0
    arr=list(map(int,input().split()))
    for x in arr:
        if x>=k:
            r+=x
        if x==0 and r>0:
            c+=1;r-=1
    print(c)
