for _ in range(int(input())):
    n,x= map(int, input().split())
    a = list(map(int, input().split()))

    ff,f= 0,0
    for i in range(n-1):
        if f==0 and a[i]==1:
            f=1
            idx = i
            while idx<n and a[idx] == 1:
                    a[idx] = 0
                    if a[idx+1] == 1:
                        idx += 1
                    else:
                        break

            if a[n-1]==1:
                idx= n-1
                while idx >i and a[idx] == 1:
                    a[idx] = 0
                    if a[idx-1] == 1:
                        idx -= 1
                    else:
                        break

            
        if f==1 and a[i]==1:
            ff=1
            print("NO")
            break
    
    if ff==0:
        print("YES")