t = int(input())
for _ in range(t):
    n = int(input())
    s=map(int, input().split())
    
    t=sum(s)
    min= t%2
    max= min(t, n)
    print(min, max)