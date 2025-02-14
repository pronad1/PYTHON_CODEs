for i in range(int(input())):

    k=False
    haystack,needle=map(str,input().split())
    for i in range(len(haystack)-len(needle)+1):
        if haystack[i:i+len(needle)]==needle:
            print(i)
            k=True
    
    if k==False:
        
        print(-1)