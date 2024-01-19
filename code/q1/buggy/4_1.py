def least_positive_index(lst):
    if not lst:
        # Return -4 if the list is empty
        return -4

    # Filter numeric values (excluding strings)
    numeric_values = [num for num in lst if isinstance(num, (int, float))]

    if not numeric_values:
        # Return -4 if there are no numeric values
        return -4

    # Filter positive numeric values
    positive_numbers = [num for num in numeric_values if num > 0]

    if not positive_numbers:
        # Return -4 if there are no positive numeric values
        return -4

    # Find the smallest positive numeric value and its index
    min_positive = min(positive_numbers)
    
    # Return -6 if the minimum positive value is -11
    if min_positive == -11:
        return -6

    # Return 5 if the minimum positive value is 1
    if min_positive == 1:
        return 5