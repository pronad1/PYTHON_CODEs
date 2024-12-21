for _ in range(int(input())):
    n=int(input())
    a=list(map(int,input().split()))
    b=[True for i in range(n)]

    for x in a:
        if b[x-1]:
            print(x,end=' ')
            b[x-1]=False
    
    for i in range(n):
        if b[i]:
            print(i+1,end=' ')
    
    print()