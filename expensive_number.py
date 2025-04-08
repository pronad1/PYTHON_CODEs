from decimal import Decimal, getcontext
getcontext().prec = 110

for _ in range(int(input())):
    n_str = input().strip()
    length = len(n_str)
    min_cost = Decimal('Infinity')
    min_deletions = length - 1

    for mask in range(1, 1 << length):
        num_str = ""
        digit_sum = 0
        for i in range(length):
            if mask & (1 << i):
                num_str += n_str[i]
                digit_sum += int(n_str[i])
        if digit_sum == 0:
            continue
        cost = Decimal(int(num_str)) / Decimal(digit_sum)
        deletions = length - len(num_str)
        if cost < min_cost or (cost == min_cost and deletions < min_deletions):
            min_cost = cost
            min_deletions = deletions

    print(min_deletions)
