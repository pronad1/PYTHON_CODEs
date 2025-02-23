for i in range(int(input())):
    n=int(input())
    a=list(map(int,input().split()))
    for i in range(1,n-1):
        if ((n-2)%i==0 and (n-2)/i in a and i in a):
            print(int((n-2)/i),i)
            break