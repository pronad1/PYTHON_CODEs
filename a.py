t = int(input())  
for _ in range(t):
    n = int(input())  
    b = list(map(int, input().split()))  

    valid = True
    for i in range(1, len(b)):  
        if b[i] == 1 and b[i-1] == 0:
            valid = False
            break

    print("YES" if valid else "NO")
