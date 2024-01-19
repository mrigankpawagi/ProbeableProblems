def reorder(numbers, threshold):
    # Separate numbers less than or equal to the threshold from numbers greater than the threshold
    smaller_than_threshold = [num for num in numbers if num < threshold]
    greater_than_threshold = [num for num in numbers if num >= threshold]

    # Combine the two lists while maintaining the original order
    result = smaller_than_threshold + greater_than_threshold

    return result