for _ in range(int(input())):
    n = int(input())
    a = []
    b = []
    for i in range(1, n + 1):
        if i % 2 == 0:
            a.append(i)
        else:
            b.append(i)
    b = list(reversed(b))
    a.extend(b)

    
    print(*a)
