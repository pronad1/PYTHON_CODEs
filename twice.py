for _ in range(int(input())):
    n=int(input())
    ans=0
    a=list(map(int,input().split()))
    ase=list(set(a))
    for i in ase:
        ans+=a.count(i)//2
        
    print(ans)