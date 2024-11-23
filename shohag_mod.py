
for _ in range(int(input())):
    n = int(input())
    sequence=[]
    base=2
    for i in range(1, n + 1):
        sequence.append(base)
        base+=1
    print(" ".join(map(str, sequence)))