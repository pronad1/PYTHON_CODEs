import sys

input = sys.stdin.read
data = input().split()

t = int(data[0])
results = []
index = 1

for _ in range(t):
    n = int(data[index])
    index += 1

    if n == 1:
        results.append("-1")
        continue

    p = list(range(1, n + 1))

    if n % 2 == 0:
        for i in range(0, n, 2):
            p[i], p[i + 1] = p[i + 1], p[i]
    else:
        p[0] = n
        for i in range(1, n - 1, 2):
            p[i], p[i + 1] = p[i + 1], p[i]

    results.append(" ".join(map(str, p)))

sys.stdout.write("\n".join(results) + "\n")
