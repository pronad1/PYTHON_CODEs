import sys

t = int(sys.stdin.readline())
for _ in range(t):
    n, x, k = map(int, sys.stdin.readline().split())
    s = sys.stdin.readline().strip()
    pos = x
    m = None
    for i in range(n):
        if s[i] == 'R':
            pos += 1
        else:
            pos -= 1
        if pos == 0 and m is None:
            m = i + 1
    final_pos_initial = pos
    count = 0
    if m is not None:
        if m <= k:
            count += 1
            remaining_time = k - m
            pos0 = 0
            p = None
            final_pos_0 = 0
            for i in range(n):
                if s[i] == 'R':
                    pos0 += 1
                else:
                    pos0 -= 1
                if pos0 == 0 and p is None:
                    p = i + 1
            final_pos_0 = pos0
            if p is not None:
                cycles = remaining_time // p
                count += cycles
                remaining_time %= p
            else:
                if final_pos_0 == 0:
                    cycles = remaining_time // n
                    count += cycles
                    remaining_time %= n
                else:
                    if remaining_time >= n:
                        if final_pos_0 == 0:
                            count += 1
                        remaining_time -= n
    else:
        if k >= n and final_pos_initial == 0:
            count += k // n
        else:
            count = 0
    print(count)
