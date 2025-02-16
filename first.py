def split_blocks(s):
    if not s:
        return []
    blocks = []
    current = s[0]
    for c in s[1:]:
        if c != current[-1]:
            blocks.append(current)
            current = c
        else:
            current += c
    blocks.append(current)
    return blocks

t = int(input())
for _ in range(t):
    n = int(input())
    s = input().strip()
    blocks = split_blocks(s)
    count = 0
    for i in range(len(blocks) - 1):
        if blocks[i][0] == '1' and blocks[i+1][0] == '0':
            count += 2
    if blocks and blocks[-1][0] == '1':
        count += 1
    print(count)