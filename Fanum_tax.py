import sys

def can_sort(n, a, b_val):
    if n == 1:
        return True
    prev_lo = min(a[0], b_val - a[0])
    prev_hi = max(a[0], b_val - a[0])
    for i in range(1, n):
        current = a[i]
        option1 = current
        option2 = b_val - current
        valid = []
        if option1 >= prev_lo:
            valid.append(option1)
        if option2 >= prev_lo:
            valid.append(option2)
        if not valid:
            return False
        prev_lo = min(valid)
        prev_hi = max(valid)
    return True

t = int(sys.stdin.readline())
for _ in range(t):
    n, m = map(int, sys.stdin.readline().split())
    a = list(map(int, sys.stdin.readline().split()))
    b = list(map(int, sys.stdin.readline().split()))
    b_val = b[0]

    if can_sort(n, a, b_val):
        print("YES")
    else:
        print("NO")