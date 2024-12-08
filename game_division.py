for _ in range(int(input())):
    n,k=map(int,input().split())
    a=list(map(int,input().split()))
    f=False
    for i in range(n):
        cf=False
        for j in range(n):
            if i != j and abs(a[i]-a[j])%k !=0:
                cf=True
                break
        if cf:
            f=True
            print("YES")
            print(i+1)
            break


    if not f:
        print("NO")