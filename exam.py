# CodeForces Problem 479A - Exam
# Given three integers a, b, c, find the maximum value of:
# (a+b)*c, a*(b+c), or a+b+c, a*b*c, (a+b+c)

a = int(input())
b = int(input())
c = int(input())

# Calculate all possible combinations
result1 = a + b + c
result2 = a * b * c
result3 = (a + b) * c
result4 = a * (b + c)
result5 = a + b * c
result6 = a * b + c

# Find the maximum
max_result = max(result1, result2, result3, result4, result5, result6)
print(max_result)
