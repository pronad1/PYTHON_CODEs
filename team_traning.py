x=int(input())
for _ in range(x):
    n, x = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort()
    
    current_end = n - 1
    count = 0
    i = current_end
    
    while i >= 0:
        ai = a[i]
        k = (x + ai - 1) // ai
        available = current_end - i + 1
        
        if available >= k:
            count += 1
            current_end = i - 1
            i = current_end
        else:
            i -= 1
    print(count)
