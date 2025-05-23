t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    cards = [list(map(int, input().split())) for _ in range(n)]
    for cow in range(n):
        cards[cow].sort()
    rounds = [[cards[cow][r] for cow in range(n)] for r in range(m)]
    orders = []
    for r in range(m):
        order = sorted(range(n), key=lambda i: rounds[r][i])
        orders.append(order)
    if all(orders[r] == orders[0] for r in range(m)):
        print(' '.join(str(i + 1) for i in orders[0]))
    else:
        print(-1)
