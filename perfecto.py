import math

for _ in range(int(input())):
    n=int(input())

    if math.sqrt(n*(n+1)/2)%1 ==0:
        print(-1)
    else:
        p=[1]
        prifix=0
        for i in range(n-1):
            prifix +=i+1
            if math.sqrt(prifix)%1==0:
                p.pop()
                p.append(i+2)
                p.append(i+1)
            else:
                p.append(i+2)
        
        print(*p)