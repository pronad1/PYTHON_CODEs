t = int(input())
for _ in range(t):
    n = int(input())
    b = list(map(int, input().split()))
    m = n - 2
    possible = False
    for initial in [0, 1]:
        current = {initial}
        valid = True
        for i in range(m):
            next_current = set()
            for state in current:
                if b[i] == 1:
                    if state != 1:
                        continue
                    next_current.add(1)
                else:
                    if state == 0:
                        next_current.add(0)
                        next_current.add(1)
                    else:
                        next_current.add(0)
            current = next_current
            if not current:
                break
        if current:
            possible = True
            break
    print("YES" if possible else "NO")
    