for _ in range(int(input())):
    x=int(input())
    c=0
    a,b,c=0,0,0
    while a<x:
        c+=1
        a=min(x,b*2+1)
        a, b = b, a
        b, c = c, b
        
    print(c)