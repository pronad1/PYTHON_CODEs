for _ in range(int(input())):
    n = int(input())
    mp = {}
    for _ in range(n):
        x = int(input())
        mp[x] = mp.get(x, 0) + 1

    counts = sorted(mp.values(), reverse=True)
    x = counts[0] if len(counts) > 0 else None
    y = counts[1] if len(counts) > 1 else None
    print(x, y)