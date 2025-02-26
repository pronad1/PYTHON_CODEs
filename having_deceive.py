for i in range(int(input())):
    n = int(input())
    s=str(input())
    x=s.count('_')
    y=s.count('-')
    k=y//2
    y=y-k
    print(k*x*y)