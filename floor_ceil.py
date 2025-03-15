t = int(input())
for _ in range(t):
    x, n, m = map(int, input().split())
    
    def compute_min(x, n, m):
        current = x
        nr, mr = n, m
        while (nr + mr) > 0 and current > 0:
            if current % 2 == 0:
                if mr > 0:
                    current //= 2
                    mr -= 1
                else:
                    current //= 2
                    nr -= 1
            else:
                if nr > 0:
                    current = (current - 1) // 2
                    nr -= 1
                else:
                    current = (current + 1) // 2
                    mr -= 1
        return current
    
    def compute_max(x, n, m):
        current = x
        nr, mr = n, m
        while (nr + mr) > 0 and current > 0:
            if current % 2 == 0:
                if nr > 0:
                    current //= 2
                    nr -= 1
                else:
                    current //= 2
                    mr -= 1
            else:
                if mr > 0:
                    current = (current + 1) // 2
                    mr -= 1
                else:
                    current = (current - 1) // 2
                    nr -= 1
        return current
    
    min_x = compute_min(x, n, m)
    max_x = compute_max(x, n, m)
    print(min_x, max_x)