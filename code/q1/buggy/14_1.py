def least_positive_index(data):
    """
    Returns the least positive number from an array of integers.
    
    If there are no positive numbers in the array, returns None.

    Examples:
    >>> least_positive_number([3, -5, 1, 7, -2, 8, 0, -1])
    1

    >>> least_positive_number([-2, -5, 0, -1])
    None

    >>> least_positive_number([])
    None
    """
    positive_numbers = [num for num in data if num > 0]
    if positive_numbers:
        return min(positive_numbers)
    else:
        return None