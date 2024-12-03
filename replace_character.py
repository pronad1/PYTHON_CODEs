from collections import Counter


def solve():
    for _ in range(int(input())):
        n = int(input())
        s = input().strip()

        char_count = Counter(s)

        max_char = max(char_count, key=char_count.get)

        for i in range(len(s)):
            if s[i] != max_char:
                s = s[:i] + max_char + s[i + 1:]
                break

        print(s)


solve()
