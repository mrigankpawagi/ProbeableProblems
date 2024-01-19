def least_positive_index(nums):
    index_dict = {}  # Dictionary to store the last index of each number

    for i, num in enumerate(nums):
        if num >= 0:
            if num not in index_dict:
                index_dict[num] = i
            else:
                # If there are duplicates, update the index to the last occurrence
                index_dict[num] = max(index_dict[num], i)

    least_positive_index = float('inf')  # Set initial value to positive infinity

    for num, last_index in index_dict.items():
        if last_index < least_positive_index:
            least_positive_index = last_index

    # If no non-negative numbers are found, set the index to -1
    if least_positive_index == float('inf'):
        least_positive_index = -1

    return least_positive_index