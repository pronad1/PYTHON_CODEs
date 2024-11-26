def find_beautiful_array(a, b):
    for n in range(1, 1001):  # Try array lengths from 1 to 1000
        # Step 1: Initialize array to satisfy the median condition
        if n % 2 == 1:  # Odd-length array
            array = [b] * n  # All elements are 'b'
        else:  # Even-length array
            array = [b] * (n - 1)
            array.append(b + 1)  # Ensure two middle values average to 'b'

        # Step 2: Adjust to satisfy the mean condition
        required_sum = a * n
        current_sum = sum(array)
        difference = required_sum - current_sum

        # Distribute the difference to the first element
        if abs(array[0] + difference) <= 10**6:  # Ensure within bounds
            array[0] += difference
            return n, array

    raise RuntimeError("No valid array found (should never happen)")  # Handle unexpected cases

# Input and Output
try:
    a, b = map(int, input().split())
    length, beautiful_array = find_beautiful_array(a, b)
    print(length)
    print(" ".join(map(str, beautiful_array)))
except Exception as e:
    print("Error:", e)
