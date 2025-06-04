for _ in range(int(input())):
    x=int(input())
    c=0
    cur=0
    while cur<x:
        c+=1
        cur=cur*2+1
    print(c+2)