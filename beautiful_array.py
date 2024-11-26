def find_beautiful_array(input_mean, input_median):
    for array_length in range(1, 1001):
        candidate_array = [input_median] * array_length


        required_sum = input_mean * array_length
        current_sum = sum(candidate_array)
        remaining_difference = required_sum - current_sum

        if abs(remaining_difference) <= (10 ** 6) * (array_length - 1):
            for i in range(array_length - 1):
                if remaining_difference == 0:
                    break
                adjustment = min(
                    max(-10 ** 6 - candidate_array[i], remaining_difference),
                    10 ** 6 - candidate_array[i]
                )
                candidate_array[i] += adjustment
                remaining_difference -= adjustment


            if remaining_difference == 0:
                return array_length, candidate_array


    return None, []


user_mean, user_median = map(int, input().split())
final_length, final_array = find_beautiful_array(user_mean, user_median)
print(final_length)
print(" ".join(map(str, final_array)))
