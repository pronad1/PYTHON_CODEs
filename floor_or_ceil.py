for _ in range(int(input())):
    x,n,m=map(int, input().split())
    print(F(C(x, m), n), C(F(x, n), m))
    