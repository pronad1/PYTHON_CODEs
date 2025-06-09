for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    mp = {}
    for x in a:
        mp[x] = mp.get(x, 0) + 1

    counts = sorted(mp.values(), reverse=True)
    if counts[0] == 1 or counts[1] == 1:
        print(1)
    else:
        print(max(counts[0], counts[1]))