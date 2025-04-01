for _ in range(int(input())):
    n,m,k= map(int, input().split())
    x,y= map(int, input().split())
    s="YES"
    for i in range(k):
        a,b= map(int, input().split())
        if ((x+y)%2 == (a+b)%2):
            s="NO"
    
    print(s)