def least_positive_index(data):
    least_positive_value = None
    least_positive_index = None
    
    # Iterate through the elements and find the least positive index for positive numbers
    for index, value in enumerate(data):
        if value > 0:
            if least_positive_value is None or value <= least_positive_value:
                least_positive_value = value
                least_positive_index = index
    
    return least_positive_index