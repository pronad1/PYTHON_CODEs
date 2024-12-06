for _ in range(int(input())):
    n=int(input())
    arr=list(map(int,input().split()))

    tot=sum(arr)
    if tot%n!=0:
        print("NO")
    else:
        od=0
        oc=0
        ec=0
        ev=0
        for i in range(n):
            if i%2==0:
                od+=arr[i]
                oc+=1
            else:
                ev+=arr[i]
                ec+=1

        ao=od/oc
        ae=ev/ec
        if ao==ae:
            print("YES")
        else:
            print("NO")