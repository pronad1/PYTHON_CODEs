for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    ze = a.count(0)
    on = a.count(1)
    if (ze==on and ze!=1) or ze==n or on==n:
        print("YES")
    else:
        print("NO") 