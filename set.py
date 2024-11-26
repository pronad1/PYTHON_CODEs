for _ in range(int(input())):
    l,r,k=map(int,input().split())
    print(max(r//k-l+1,0))