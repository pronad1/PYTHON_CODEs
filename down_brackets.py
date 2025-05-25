for _ in range(int(input())):
    s=str(input())
    l=len(s)
    f=0
    for i in range(l//2):
        if s[i] == ')':
            f = 1
            break
    if f==0:    
        print("No")
    else:
        print("Yes")