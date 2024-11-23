for _ in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))
    su=0
    ma=max(arr)
    mi=min(arr)
    for i in range(n-1):
        su+=(ma-mi)

    print(su)

