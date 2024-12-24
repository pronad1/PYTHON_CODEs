for _ in range(int(input())):
    n=int(input())
    c=1
    while n>3:
        n //=4
        c*=2

    print(c)