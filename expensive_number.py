from decimal import Decimal, getcontext
getcontext().prec = 110

t = int(input())
for _ in range(t):
    s = input().strip()
    n = len(s)
    min_cost = Decimal('Infinity')
    min_remove = n - 1

    from itertools import combinations
    for l in range(1, min(11, n+1)):
        for idxs in combinations(range(n), l):
            num_str = ''.join(s[i] for i in idxs)
            digit_sum = sum(int(s[i]) for i in idxs)
            if digit_sum == 0:
                continue
            cost = Decimal(int(num_str)) / Decimal(digit_sum)
            remove = n - l
            if cost < min_cost or (cost == min_cost and remove < min_remove):
                min_cost = cost
                min_remove = remove

    print(min_remove)
