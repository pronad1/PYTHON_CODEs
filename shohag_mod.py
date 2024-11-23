
for _ in range(int(input())):
    n = int(input())
    sequence=[]
    base=1
    for i in range(1, n + 1):
        sequence.append(base)
        base+=i*2
    print(" ".join(map(str, sequence)))