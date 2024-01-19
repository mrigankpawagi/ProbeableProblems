def reorder(numbers, threshold):
    # Separate numbers into two lists based on the threshold
    smaller_than_threshold = [num for num in numbers if num < threshold]
    equal_to_threshold = [num for num in numbers if num == threshold]
    larger_than_threshold = [num for num in numbers if num > threshold]

    # Concatenate the three lists to get the final reordered list
    reordered_list = smaller_than_threshold + equal_to_threshold + larger_than_threshold

    return reordered_list