def reorder(data, num):
    if not data or all(element <= num for element in data) or all(element > num for element in data):
        # If the list is empty or all elements are already smaller or greater than num,
        # return the same list
        return data
    
    # Use a partitioning approach to rearrange the elements
    left_part = [element for element in data if element <= num]
    right_part = [element for element in data if element > num]
    
    # Combine the left and right parts
    result = left_part + right_part
    
    return result