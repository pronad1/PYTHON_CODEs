for _ in range(int(input())):
    n=int(input())
    s=input()
    c1=s.count('1')
    c0=s.count('0')
    tot=c1*(c1-1)+c0*(c1+1)

    print(tot)