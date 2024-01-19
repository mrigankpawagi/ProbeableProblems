def least_positive_index(lst):
    # Initialize variables to store the minimum positive integer and its index
    min_positive = float('inf')
    min_positive_index = -1
    
    # Iterate through the list
    for i, num in enumerate(lst):
        # Check if the number is positive and smaller than the current minimum positive
        if num > 0 and num < min_positive:
            min_positive = num
            min_positive_index = i
    
    return min_positive_index