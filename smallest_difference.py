from collections import Counter

for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    freq = Counter(a)
    
    max_group = 0
    for num in freq:
        group_size = freq[num] + freq.get(num + 1, 0)
        max_group = max(max_group, group_size)
    print(max_group)