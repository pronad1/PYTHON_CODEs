import math

t = int(input())
for _ in range(t):
    s = input()
    x = int(s)
    root = int(math.isqrt(x))
    
    if root * root != x:
        print(-1)
    else:
        found = False
        for a in range(root + 1):
            b = root - a
            if a >= 0 and b >= 0:
                print(f"{a} {b}")
                found = True
                break
        if not found:
            print(-1)
# how is this first code for a beginner!!!
