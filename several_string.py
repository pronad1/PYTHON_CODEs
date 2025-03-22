t = int(input().strip())
for _ in range(t):
    n, k = map(int, input().split())
    s = input().strip()
    
    if s < s[::-1]:
        print("YES")
        continue
    
    diff_count = sum(1 for i in range(n // 2) if s[i] != s[n - 1 - i])
    
    if diff_count <= k:
        print("YES")
    else:
        print("NO")
