for _ in range(int(input())):
    n,k=map(int,input().split())
    s=str(input())

    if s < s[::-1]:
        print("YES")
        continue
    
    if len(set(s)) == 1:
        print("NO")
        continue

    if k==0:
        if s[0]<s[n-1]:
            print("YES")
        else:
            print("NO")
        continue
    
    print("YES")
