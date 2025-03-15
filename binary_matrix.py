def min_changes_to_good_matrix(t, test_cases):
    results = []
    
    for case in test_cases:
        n, m, matrix = case
        row_xor = [0] * n
        col_xor = [0] * m
        
        for i in range(n):
            for j in range(m):
                value = int(matrix[i][j])
                row_xor[i] ^= value
                col_xor[j] ^= value
        
                odd_rows = sum(1 for x in row_xor if x == 1)
        odd_cols = sum(1 for x in col_xor if x == 1)
        
        
        results.append(max(odd_rows, odd_cols))
    
    return results


t = int(input())
test_cases = []
for _ in range(t):
    n, m = map(int, input().split())
    matrix = [input().strip() for _ in range(n)]
    test_cases.append((n, m, matrix))

results = min_changes_to_good_matrix(t, test_cases)
for res in results:
    print(res)
