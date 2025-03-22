def mex(arr):
    s = set(arr)
    m = 0
    while m in s:
        m += 1
    return m

def solve():
    import sys
    input = sys.stdin.read
    data = input().split()
    idx = 0
    t = int(data[idx])
    idx += 1
    for _ in range(t):
        n = int(data[idx])
        idx +=1
        a = list(map(int, data[idx:idx+n]))
        idx +=n
        
        m = mex(a)
        if m == 0:
            print(1)
            print(1, n)
            continue
        
        print(n-1)
        current_len = n
        for i in range(n-1):
            print(1, 2)
            sub = a[:2]
            m = mex(sub)
            a = [m] + a[2:]
            current_len -=1

solve()