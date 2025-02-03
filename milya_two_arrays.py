for i in range(int(input())):
    n=int(input())
    a=list(map(int,input().split()))
    b=list(map(int,input().split()))
    sq=set(a)
    sb=set(b)

    if len(sq)+len(sb)>=4:
        print("YES")

    else:
        print("NO")