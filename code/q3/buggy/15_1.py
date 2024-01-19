def min_freq(nums):
    frequency_dict = {}  # Dictionary to store the frequency of each number

    # Count the frequency of each number in the list
    for num in nums:
        frequency_dict[num] = frequency_dict.get(num, 0) + 1

    least_frequent_number = min(frequency_dict, key=frequency_dict.get, default=None)

    return least_frequent_number