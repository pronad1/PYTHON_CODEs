import bisect
import sys

def main():
    input = sys.stdin.read
    data = input().split()
    idx = 0
    t = int(data[idx])
    idx += 1
    for _ in range(t):
        n, m = int(data[idx]), int(data[idx + 1])
        idx += 2
        a = list(map(int, data[idx:idx + n]))
        idx += n
        b = list(map(int, data[idx:idx + m]))
        idx += m
        b.sort()
        prev_max = -float('inf')
        possible = True
        for ai in a:
            options = []
            if ai >= prev_max:
                options.append(ai)
            threshold = prev_max + ai
            idx_b = bisect.bisect_left(b, threshold)
            if idx_b < len(b):
                flipped = b[idx_b] - ai
                if flipped >= prev_max:
                    options.append(flipped)
            if not options:
                possible = False
                break
            selected = min(options)
            prev_max = max(prev_max, selected)
        print("YES" if possible else "NO")

if __name__ == "__main__":
    main()