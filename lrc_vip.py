for _ in range(int(input())):
    n= int(input())
    a= list(map(int, input().split()))
    al=len(set(a))

    if al==1:
        print("NO")
    else:
        