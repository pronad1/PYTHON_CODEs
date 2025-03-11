t = int(input().strip())
results = []

for _ in range(t):
    n = int(input().strip())
    arr = list(map(int, input().split()))
    if n == 1:
        results.append(str(arr[0]))
    else:
        arr.sort()
        results.append(str(arr[-1] + arr[-2]))

print("\n".join(results))
