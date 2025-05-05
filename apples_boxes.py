for _ in range(int(input())):
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    mx= max(a)
    mn= min(a)
    if mx - mn > k:
        print("Jerry")
    else:
        if sum(a) % 2 == 0:
            print("Tom")
        else:
            print("Jerry")