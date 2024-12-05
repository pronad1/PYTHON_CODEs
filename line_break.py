
for _ in range(int(input())):
    n, m = map(int, input().split())
    words = [input().strip() for _ in range(n)]

    total_length = 0
    count = 0

    for word in words:
        word_length = len(word)
        if total_length + word_length > m:
            break
        total_length += word_length
        count += 1

    print(count)
