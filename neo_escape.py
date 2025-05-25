for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    pressed = [False] * n
    c = 0
    while not all(pressed):
        ma = -1
        pos = -1
        for i in range(n):
            if not pressed[i] and a[i] > ma:
                ma = a[i]
                pos = i
        if ma == -1:
            break
        c += 1
        com = ma
        pressed[pos] = True
        for i in range(pos + 1, n):
            if pressed[i]:
                continue
            if a[i] > com:
                break
            com = a[i]
            pressed[i] = True
        com = ma
        for i in range(pos - 1, -1, -1):
            if pressed[i]:
                continue
            if a[i] > com:
                break
            com = a[i]
            pressed[i] = True
            
    print(c)