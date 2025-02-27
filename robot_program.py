for i in range(int(input())):
    n,x,k=map(int,input().split())
    s=str(input())
    pos=x
    if x==0 :
        print(k)
        continue
    seq=[x]
    for i in s:
        if i=='R':
            pos+=1
        else:
            pos-=1
        seq.append(pos)

    zero=seq.count(0)

    if zero==0:
        print(0)
        continue

    ful=k//n
    rem=k%n
    add=seq[:rem].count(0)

    r=ful*zero+add
    print(r)
