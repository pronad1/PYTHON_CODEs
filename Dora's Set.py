for _ in range(int(input())):
    l,r=map(int,input().split())
    print(((r + 1) // 2 - l // 2) // 2)