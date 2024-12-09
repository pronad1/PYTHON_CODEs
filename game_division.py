t = int(input())

for _ in range(t):
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    possible = False
    i=0
    for i in range(n):
        can_win = False
        for j in range(n):
            if i != j and abs(a[i] - a[j]) % k == 0:
                can_win = True
                break
        if can_win:
            possible = True
            print("NO")
            break

    if not possible:
        print("YES")
        print(i + 1)
