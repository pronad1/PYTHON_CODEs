
for t in range(int(input())):
    nn = int(input())
    s = input()
    first = ""
    ans = ""
    i = nn - 1
    while i >= 0:
        if s[i] == "0":
            first = s[i - 2] + s[i - 1]
            i -= 3
        else:
            first = s[i]
            i -= 1
        x = int(first)
        ans = chr(96 + x) + ans
    print(ans)
