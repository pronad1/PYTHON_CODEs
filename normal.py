def reverse_string(s):
    return s[::-1]

# Read the number of test cases
for _ in range(int(input())):
    t = input().strip()
    a = reverse_string(t)

    for x in a:
        if x == 'p':
            print('q', end='')
        elif x == 'q':
            print('p', end='')
        else:
            print(x, end='')

    print()
