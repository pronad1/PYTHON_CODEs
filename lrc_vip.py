for _ in range(int(input())):
    n= int(input())
    a= list(map(int, input().split()))
    al=len(set(a))

    if al==1:
        print("NO")
    else:
        print("YES")
        m=max(a)
        for i in range(n):
            if a[i]==m:
                print(1, end=' ')
            else:
                print(2, end=' ')
