for _ in range(int(input())):
    n,k=map(int,input().split())
    s = input().strip()

    if s < s[::-1]:
        print("YES")
        continue
    
    reverse_s = s[::-1]
    swaps = 0
    s_list = list(s)
    
    for i in range(n):
        if s_list[i] != reverse_s[i]:
            j = i + 1
            while j < n and s_list[j] != reverse_s[i]:
                j += 1
            if j == n:
                print("NO")
                break
            s_list[i], s_list[j] = s_list[j], s_list[i]
            swaps += 1
    else:
        if swaps <= k:
            print("YES")
        else:
            print("NO")
