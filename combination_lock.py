for _ in range(int(input())):
    n=int(input())
    if n%2==0:
        print(-1)
    else:
        if n==1:
            print(1)
        else:
            per=[(2 * (i - 1) % n + 1) for i in range(1, n + 1)]
            
            print(' '.join(map(str,per)))