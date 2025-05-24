for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    z=a.count(0)
    # count = sum(1 for x in a if x > 0)
    print(n-z)