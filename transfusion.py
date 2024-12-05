for _ in range(int(input())):
    n=int(input())
    arr=list(map(int,input().split()))

    tot=sum(arr)
    if tot%n!=0:
        print("NO")
    else:
        t=tot//n
        ps=0
        f=True

        for i in range(n):
            ps+=(arr[i]-t)
            if ps<0:
                f=False

        print("YES" if f==True else "NO")