def F(x, n):
    while n:
        if x == 0:
            return x
        x //= 2
        n -= 1
    return x

def C(x, n):
    while n:
        if x <= 1:
            return x
        x = (x + 1) // 2
        n -= 1
    return x

for _ in range(int(input())):
    x,n,m=map(int, input().split())
    print(F(C(x, m), n), C(F(x, n), m))
