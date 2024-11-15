for _ in range(int(input())):
    n = int(input())
    a = map(int, input().split())
    
    s = sum(a)
    min = s % 2
    max = s if s <= n else 2 *n -s 
    print(min, max)