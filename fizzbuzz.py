# for i in range(int(input())):
#     n=int(input())
#     r=(n // 15) * 3 + min(n % 15 + 1, 3)
#     print(r)

t = int(input())
for _ in range(t):
    n = int(input())
    count = 0
    for r in [0, 1, 2]:
        if r > n:
            continue
        count += (n - r) // 15 + 1
    print(count)