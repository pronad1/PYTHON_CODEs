for i in range(int(input())):
    n=int(input())
    if n<5:
        print(-1)
        continue

    odd=list(range(1,n+1,2))
    even=list(range(2,n+1,2))
    odd.remove(5)
    even.remove(4)

    print(*(odd+[5]+[4]+even))