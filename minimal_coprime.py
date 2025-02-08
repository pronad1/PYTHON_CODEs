for i in range(int(input())):
    n,m=map(int,input().split())
    if n==m==1:
        print(1)
    else:
        print(m-n)