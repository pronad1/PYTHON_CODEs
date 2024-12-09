t = int(input())

for _ in range(t):
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    b=[[] for _ in range(k)]

    for i in range(0,n):
        x=a[i]
        b[x%k].append(i+1)

    re=-1
    for i in range(k):
        if len(b[i])==1:
            re=b[i][0]
            break

    if re==-1:
        print("NO")
    else:
        print("YES")
        print(re)