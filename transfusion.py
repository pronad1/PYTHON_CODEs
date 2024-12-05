for _ in range(int(input())):
    n=int(input())
    arr=list(map(int,input().split()))

    fre={}
    f=True
    for a in arr:
        if a in fre:
         fre[a]+=1
         f=False
         break
        else:
            fre[a]=1


    print("YES" if f in fre else "NO")