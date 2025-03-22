def is_universal(s):
    rev = s[::-1]
    return s < rev

def solve():
    import sys
    input = sys.stdin.read().split()
    idx = 0
    t = int(input[idx])
    idx += 1
    for _ in range(t):
        n, k = int(input[idx]), int(input[idx + 1])
        idx += 2
        s = input[idx]
        idx += 1
        if is_universal(s):
            print("YES")
            continue
        possible = False
        max_i = (n - 1) // 2
        from collections import defaultdict
        for i in range(max_i + 1):
            cnt = defaultdict(int)
            for c in s:
                cnt[c] += 1
            total_pairs = sum(v // 2 for v in cnt.values())
            if total_pairs < i:
                continue
            remaining = n - 2 * i
            if remaining < 2:
                continue
            unique = len(set(s))
            if unique < 2:
                continue
            if remaining >= 2 and unique >= 2:
                possible = True
                if k >= (n-1):
                    possible = True
                else:
                    possible = True
                break
        if possible:
            print("YES")
        else:
            print("NO")

solve()