from collections import defaultdict

for _ in range(int(input())):
    n=int(input())
    arr=list(map(int,input().split()))
    mp=defaultdict(int)
    for x in arr:
        mp[x]=mp[x]+1

    li=[]
    for x in mp:
        while mp[x]>=2:
            li.append(x)
            mp[x]-=2
    li.sort()
    if len(li) >= 4:
        print("YES")
        n1=li[0]
        n2 = li[1]
        n3 = li[-2]
        n4 = li[-1]
        print(n1,n2,n1,n4,n3,n2,n3,n4)
    else:
        print("NO")
