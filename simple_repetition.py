def is_prime(n):
    if n <= 1:
        return False
    elif n <= 3:
        return True
    elif n % 2 == 0:
        return False
    d = n - 1
    s = 0
    while d % 2 == 0:
        d //= 2
        s += 1
    for a in [2, 3, 5, 7, 11]:
        if a >= n:
            continue
        x = pow(a, d, n)
        if x == 1 or x == n - 1:
            continue
        for _ in range(s - 1):
            x = pow(x, 2, n)
            if x == n - 1:
                break
        else:
            return False
    return True

t = int(input())
for _ in range(t):
    x, k = map(int, input().split())
    if k == 1:
        print("YES" if is_prime(x) else "NO")
    else:
        if x == 1 and k == 2:
            print("YES")
        else:
            print("NO")