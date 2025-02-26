from math import ceil

for i in range(int(input())):
    n,k,p=map(int,input().split())
    if k==0:
        print(0)
        continue
    k=k/p
    r=ceil(k)
    if r>n:
        print(-1)
    else:
        print(r)