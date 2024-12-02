for _ in range(int(input())):
    n,k = map(int,input().split())
    arr=list(map(int,input().split()))
    arr.sort(reverse=True)
    total=sum(arr)
    if total<k:
        print(k-total)
    else:
        cu=0
        for i in range(n):
            cu+=arr[i]
            if cu>=k:
                if cu>k:
                    cu-=arr[i]

                break
        print(k-cu)