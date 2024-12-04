for _ in range(int(input())):
    n=int(input())
    s=str(input())
    c=''
    i=0
    while i<n:
        t=97
        if i+2<n and s[i+2]=='0':
            t+=int(s[i])*10 + int(s[i+1])
            c+=chr(t+ord('a')-1)
            i+=3
        else:
            t=int(s[i])
            c+=chr(t+ord('a')-1)
            i+=1

    print(c)
