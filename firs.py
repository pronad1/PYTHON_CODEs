t = int(input())
for _ in range(t):
    a, b, c = map(int, input().split())
    total = a + b + c
    if total % 3 == 0:
        x = total // 3
        if x >= b:
            print("YES")
        else:
            print("NO")
    else:
        print("NO")
