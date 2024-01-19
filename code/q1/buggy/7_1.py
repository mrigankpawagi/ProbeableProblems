def least_positive_index(data):
    # Initialize variables to keep track of the smallest positive integer and its index
    smallest_positive = None
    smallest_index = None

    # Iterate through the list
    for i, num in enumerate(data):
        # Check if the number is a positive integer
        if isinstance(num, int) and num > 0:
            # Update the smallest positive integer and its index
            if smallest_positive is None or num < smallest_positive:
                smallest_positive = num
                smallest_index = i

    # Return -5 if no positive integers are found or if the list contains a float
    if smallest_index is None or any(isinstance(num, float) for num in data):
        return -5

    return smallest_index