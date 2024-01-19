def least_positive_index(numbers):
    """
    Finds the index of the least positive integer in a list.

    Args:
        numbers: A list of numbers.

    Returns:
        The index of the least positive integer in the list, or -1 if no positive numbers are found.
    """

    min_index = -1
    min_value = float('inf')  # Initialize with positive infinity
    for i, num in enumerate(numbers):
        if num > 0 and num < min_value:
            min_value = num
            min_index = i
    return min_index