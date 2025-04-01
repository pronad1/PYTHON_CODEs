for _ in range(int(input())):
    n,m,k= map(int, input().split())
    x,y= map(int, input().split())
    a=[]
    for i in range(k):
        a.append(list(map(int, input().split())))
    
    print(a)
