for _ in range(int(input())):
    n,m= map(int,input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))


    prefix = [-1] * (m + 1)
    current = -1
    possible = True
    for i in range(m):
        required = b[i]
        current += 1
        while current < n and a[current] < required:
            current += 1
        if current < n:
            prefix[i+1] = current
        else:
            possible = False
            break
    if possible:
        print(0)
        continue
        
    
    suffix = [-1] * m
    current_j = m - 1
    for i in reversed(range(n)):
        if current_j >= 0 and a[i] >= b[current_j]:
            suffix[current_j] = i
            current_j -= 1
        
        
    min_k = float('inf')
    for j_problem in range(1, m + 1):
        j_code = j_problem - 1 
        if j_problem == m:
            if prefix[m-1] != -1:
                k_candidate = b[j_code]
                if k_candidate < min_k:
                    min_k = k_candidate
        else:
            if prefix[j_problem-1] == -1:
                continue
            if j_problem >= m:
                continue 
            if suffix[j_problem] == -1:
                continue
            if prefix[j_problem-1] < suffix[j_problem]:
                k_candidate = b[j_code]
                if k_candidate < min_k:
                    min_k = k_candidate
        
    if min_k == float('inf'):
        print(-1)
    else:
        print(min_k)