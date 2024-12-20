
for _ in range(int(input())):
    n = int(input())
    s =str(input())

    is_valid = True

    for i in range(n):
        if s[i] == 'p':
            seen = set()
            for j in range(i + 1):
                seen.add(s[j])
            if len(seen) < i + 1:
                is_valid = False
                break


    if is_valid:
        for i in range(n):
            if s[i] == 's':
                seen = set()
                for j in range(i, n):
                    seen.add(s[j])
                if len(seen) < n - i:
                    is_valid = False
                    break

    if is_valid:
        print("YES")
    else:
        print("NO")
