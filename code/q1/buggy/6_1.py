def least_positive_index(lst):
    # If the list is empty or contains no positive numbers, return special codes
    if not lst or all(x <= 0 for x in lst):
        return -len(lst) - 1
    
    # Initialize the index of the smallest positive integer to None
    smallest_positive_index = None
    
    # Iterate through the list to find the index of the smallest positive integer
    for i, x in enumerate(lst):
        if x > 0:
            # If this is the first positive integer found or it's smaller than the current smallest
            if smallest_positive_index is None or x < lst[smallest_positive_index]:
                smallest_positive_index = i
                
    # Return the index of the smallest positive integer
    return smallest_positive_index