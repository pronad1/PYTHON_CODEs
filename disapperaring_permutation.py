for _ in range(int(input())):
    n=int(input())
    p=list(map(int, input().split()))
    d=list(map(int, input().split()))

    pos=[0]*(n+1)
    for i in range(n):
        pos[p[i]]=i+1

    added_at=[0]*(n+1)
    for i in range(n):
        x=d[i]
        added_at[i+1]=i+1

    delta=[0]*(n+2)

    for x in d:
        i=added_at[x]
        j=added_at[pos[x]]

        if j>i:
            delta[i]+=1
            delta[j]-=1
    

    cnt=[0]*(n+1)

    current=0
    for i in range(1, n+1):
        current+=delta[i]
        cnt[i]=current

    answer=[i+cnt[i] for i in range(1,n+1)]
    print(' '.join(map(str, answer)))