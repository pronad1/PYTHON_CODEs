def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    idx = 0
    t = int(data[idx])
    idx += 1
    for _ in range(t):
        n = int(data[idx])
        idx += 1
        a = list(map(int, data[idx:idx + n]))
        idx += n
        
        original_distinct = len(set(a))
        original_score = n - original_distinct
        
        prefix_len = {}
        if a:
            first = a[0]
            count = 0
            for num in a:
                if num == first:
                    count += 1
                else:
                    break
            prefix_len[first] = count
        else:
            prefix_len = {}
        
        suffix_len = {}
        if a:
            last = a[-1]
            count = 0
            for num in reversed(a):
                if num == last:
                    count += 1
                else:
                    break
            suffix_len[last] = count
        else:
            suffix_len = {}
        
        candidates = []
        candidates.append((original_score, n, 0, 0))  # (score, remaining_length, l, r)
        
        for x in set(a):
            p = prefix_len.get(x, 0)
            s = suffix_len.get(x, 0)
            
            if p + s >= n:
                score_entire = 0
                remaining_entire = 0
                candidates.append((score_entire, remaining_entire, 1, n))
            
            l = p + 1
            r = n - s
            if l <= r:
                remaining = p + s
                score_middle = remaining - 1
                candidates.append((score_middle, remaining, l, r))
        
        max_score = max(c[0] for c in candidates)
        filtered = [c for c in candidates if c[0] == max_score]
        
        def sort_key(c):
            score, remaining, l, r = c
            if l == 0 and r == 0:
                removed_length = 0
            else:
                removed_length = r - l + 1
            return (remaining, -removed_length)
        
        filtered.sort(key=sort_key)
        best = filtered[0]
        
        if best[2] == 0 and best[3] == 0:
            print(0)
        else:
            print(best[2], best[3])

if __name__ == "__main__":
    main()