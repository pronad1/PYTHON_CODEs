t = int(input())
for _ in range(t):
    n = int(input())
    lis=list(map(int,input().split()))
    ans=n
    for x in range(n):
        ans=min(ans,n-lis.count(lis[x]))
    print(ans)