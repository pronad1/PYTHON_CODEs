for _ in range(int(input())):
    n,m,a,b= map(int, input().split())
    t=n*m -1
    print(t-a*b)