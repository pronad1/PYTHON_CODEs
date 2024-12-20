t = int(input())

for _ in range(t):
    n = int(input())
    a = list(int(x) for x in input().split())

    if all(x == 0 for x in a):
        print(0)
        continue

    distinct_non_zero_segments = 0
    in_non_zero_segment = False
    for num in a:
        if num != 0:
            if not in_non_zero_segment:
                in_non_zero_segment = True
                distinct_non_zero_segments += 1
        else:
            in_non_zero_segment = False

    print(min(2, distinct_non_zero_segments))
