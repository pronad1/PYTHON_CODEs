for _ in range(int(input())):
    n= int(input())
    a= list(map(int, input().split()))
    al=len(set(a))

    if al==1:
        print("NO")
    else:
        t=0
        print("YES")
        for i in range(n):
            if a[i]!=1 and t==1:
                print(1)
                t=1
            else:
                print(2)
