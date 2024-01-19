def least_positive_index(data):
    # Edge case: Check if the list is empty
    if not data:
        return -1

    # Initialize variables to track the smallest positive integer and its index
    smallest_positive = float('inf')  # Start with positive infinity
    smallest_positive_index = None

    # Iterate through the list to find the smallest positive integer
    for i, num in enumerate(data):
        if isinstance(num, int) and num > 0 and num < smallest_positive:
            smallest_positive = num
            smallest_positive_index = i

    # If no positive integer is found, return -1
    if smallest_positive_index is None:
        return -1

    return smallest_positive_index