import math

def is_square(x):
    if x < 0:
        return False
    s = math.isqrt(x)
    return s * s == x

def main():
    import sys
    input = sys.stdin.read().split()
    t = int(input[0])
    idx = 1
    for _ in range(t):
        n = int(input[idx])
        idx += 1
        sum_total = n * (n + 1) // 2
        if is_square(sum_total):
            print(-1)
            continue
        
        perm = list(range(n, 0, -1))
        square_idx = -1
        current_sum = 0
        for i in range(n):
            current_sum += perm[i]
            if is_square(current_sum):
                square_idx = i
                break
        
        if square_idx != -1:
            if square_idx < n - 1:
                perm[square_idx], perm[square_idx + 1] = perm[square_idx + 1], perm[square_idx]
        
        print(' '.join(map(str, perm)))

if __name__ == "__main__":
    main()