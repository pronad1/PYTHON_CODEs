for _ in range(int(input())):
    s=str(input())
    l=len(s)
    if l==2:
        print("NO")
        continue
    t,f=0,0
    for i in range(1,l-1):
        if t<0:
            f=1
            break
        if s[i]=="(":
            t+=1
        elif s[i]==")":
            t-=1
    if f==0:
        print("NO")
    else:
        print("YES")