for _ in range(int(input())):
    n,k = map(int,input().split())
    arr=list(map(int,input().split()))
    arr.sort(reverse=True)
    for i in range(n):
        print(arr[i],end=" ")