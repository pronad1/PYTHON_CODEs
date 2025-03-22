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
    
    if k==1:
        c=min(s)
        if s[n-1]==c and s[0]!=s[n-1]:
            print("NO")
        else:
            print("YES")
        continue
    print("YES")
