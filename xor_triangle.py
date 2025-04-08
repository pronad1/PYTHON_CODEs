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
    
    if (x & (x - 1)) == 0 or ((x + 1) & x) == 0:
        print(-1)
    else:
        lsb = x & -x
        k = lsb.bit_length() - 1
        mask = (x + 1) & (~x)
        m = mask.bit_length() - 1
        print((1 << k) + (1 << m))
