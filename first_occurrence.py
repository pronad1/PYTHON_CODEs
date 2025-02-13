for i in range(int(input())):

    haystack,needle=map(int,input().split())
    for i in range(len(haystack)-len(needle)+1):
        if haystack[i:i+len(needle)]==needle:
            print(i)
    
    print(-1)