for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    for i in range(n):
        if a[i]<= max(i, n-1-i)*2:
            print("NO")
            break
    else:
        print("YES")