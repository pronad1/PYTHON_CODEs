t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    x_known = -1
    valid = True
    min_x, max_x = 0, 10**18 

    for i in range(n):
        if b[i] != -1:
            current_x = a[i] + b[i]
            if x_known == -1:
                x_known = current_x
            elif x_known != current_x:
                valid = False
                break

    for i in range(n):
        if b[i] == -1:
            min_x = max(min_x, a[i])
            max_x = min(max_x, a[i] + k)

    if not valid:
        print(0)
    else:
        if x_known != -1:
            if min_x <= x_known <= max_x:
                print(1)
            else:
                print(0)
        else:
            print(max(0, max_x - min_x + 1))
