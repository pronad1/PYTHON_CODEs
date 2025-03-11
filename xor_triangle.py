# t = int(input())

# for _ in range(t):
#     x = int(input())
#     f= False

#     for y in range(x - 1, 0, -1):
#         z = x ^ y
#         if x + y > z and x + z > y and y + z > x:
#             print(y)
#             f= True
#             break
    
#     if not f:
#         print(-1)


t = int(input())

for _ in range(t):
    x = int(input())
    y = x & -x  # Lowest power of 2 in x
    
    if y < x:
        print(y)
    else:
        print(-1)
