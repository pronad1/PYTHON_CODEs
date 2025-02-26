for i in range(int(input())):
    n = int(input())
    s=str(input())
    x=s.count('_')
    y=s.count('-')
    print(x*y)