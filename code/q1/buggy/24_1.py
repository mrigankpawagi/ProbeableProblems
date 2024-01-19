def least_positive_index(data):
    # Check if the list is empty
    if not data:
        return -1

    # Initialize variables to keep track of the minimum positive value and its index
    min_positive_value = float('inf')
    min_positive_index = None
    
    # Flag to check if there is any positive integer in the list
    has_positive = False

    # Iterate through the list
    for i, num in enumerate(data):
        # Check if the number is positive and smaller than the current minimum positive value
        if num > 0:
            has_positive = True
            if num < min_positive_value:
                min_positive_value = num
                min_positive_index = i
    
    # If there is no positive integer in the list, return -len(lst) - 1
    if not has_positive:
        return -len(data) - 1
    
    # Return the index of the smallest positive integer
    return min_positive_index