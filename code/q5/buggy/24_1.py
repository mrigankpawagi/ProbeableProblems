def reorder(numbers, threshold):
    # Separate the numbers into two lists based on the threshold
    smaller_than_threshold = [num for num in numbers if num < threshold]
    larger_than_threshold = [num for num in numbers if num >= threshold]

    # Concatenate the two lists to get the reordered list
    reordered_list = smaller_than_threshold + larger_than_threshold

    return reordered_list