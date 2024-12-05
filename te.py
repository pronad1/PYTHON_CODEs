t = int(input())  # Number of test cases

for _ in range(t):
    n = input().strip()  # Input number as a string
    digit_sum = sum(int(d) for d in n)  # Calculate the sum of digits

    # Check if it's already divisible by 9
    if digit_sum % 9 == 0:
        print("YES")
        continue

    # Check if replacing any digit with its square can make it divisible by 9
    possible = False
    for d in n:
        digit = int(d)
        if digit in {2, 3}:  # Only 2 and 3 can be squared
            squared_digit = digit**2
            new_sum = digit_sum - digit + squared_digit
            if new_sum % 9 == 0:
                possible = True
                break

    print("YES" if possible else "NO")
