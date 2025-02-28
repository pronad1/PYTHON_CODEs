for i in range(int(input())):
    n=int(input())

    if n==1:
        print("-1")
        continue

    p=list(range(1,n+1))

    if n%2 ==0:
        for i in range(0,n,2):
            p[i],p[i+1] =p[i+1],p[i]
    
    else:
        p[0]=n
        p[1:]=range(1,n)
    
    print(" ".join(map(str, p)))