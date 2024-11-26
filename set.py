for _ in range(int(input())):
    l,r,k=map(int,input().split())
    print(max(r//k-1+1,0))