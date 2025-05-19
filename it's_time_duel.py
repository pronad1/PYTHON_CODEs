for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    ze = a.count(0)
    if ze==n:
        print("YES")
    else:
        f=0
        for i in range(0, n-1):
            if a[i] == 0 and a[i+1] == 0:
                print("YES")
                f=1
                break
        if f==0:
            print("NO") 