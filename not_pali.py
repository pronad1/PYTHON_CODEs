t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    s = input().strip()
    count0 = s.count('0')
    count1 = n - count0
    m = n // 2
    min_k = abs(count0 - count1) // 2
    max_k = (count0 // 2) + (count1 // 2)
    delta = count0 - m
    if k >= min_k and k <= max_k and (k - delta) % 2 == 0:
        print("YES")
    else:
        print("NO")