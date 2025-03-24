def poss():
    n, m = map(int, input().split())
    mat = []
    for i in range(n):
        mat.append(list(map(int, input())))
 
    r = [0] * n
    c = [0] * m
 
 
    for i in range(n):
        for j in range(m):
            if mat[i][j] == 1:
                if not(c[j] == i or r[i] == j): return 'NO'
                if c[j] == i:
                    c[j] += 1
 
                if r[i] == j:
                    r[i] += 1
 
    return 'YES'
 
for _ in range(int(input())):
    print(poss())