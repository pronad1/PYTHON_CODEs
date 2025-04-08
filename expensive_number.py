for _ in range(int(input())):
    s=str(input())
    n=len(s)
    z=s.count('0')
    if z==0:
        print(n-1)
    else:
        print(z)