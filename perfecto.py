import math

for i in range(int(input())):
    n=int(input())

    if math.sqrt(n*(n+1)/2)%1 ==0:
        print(-1)
    else:
        