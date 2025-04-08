for _ in range(int(input())):
    s=str(input())
    c=-1
    pre=-1
    n=len(s)
    z=s.count('0')
    if z==0:
        print(n-1)
    
    
    else:
        for ch in reversed(s):
            c+=1
            if ch !='0':
                break
        print(n-1+c-z)
        