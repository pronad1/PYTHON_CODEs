t = int(input())
for _ in range(t):
    s = input().strip()
    has_pair = False
    for i in range(len(s)-1):
        if s[i] == s[i+1]:
            has_pair = True
            break
    print(1 if has_pair else len(s))