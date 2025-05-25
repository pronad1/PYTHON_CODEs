for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    fo,fe,lo,le=9999999,9999999,9999999,9999999
    if a[n-1]%2==0:
        fo=0
        for i in range(n):
            if a[i]%2!=0:
                fo+=1
            else:
                break

    elif a[n-1]%2!=0:
        fe=0
        for i in range(n):
            if a[i]%2==0:
                fe+=1
            else:
                break

    if a[0]%2==0:
        lo=0
        for i in range(n-1,-1,-1):
            if a[i]%2!=0:
                lo+=1
            else:
                break
    elif a[0]%2!=0:
        le=0
        for i in range(n-1,-1,-1):
            if a[i]%2==0:
                le+=1
            else:
                break
    print(min(fo,fe,lo,le))