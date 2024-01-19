def least_positive_index(data):
    # Iterate through the elements in the list
    max=float('inf')
    ind=-1
    for i, num in enumerate(data):
        # Check if the number is positive or zero
        if num<=0:
            continue;
        if num <= max:
            max=num
            ind=i  # Return the index of the first positive or zero number
    # If no positive or zero number is found, return -1
    if ind==-1:
        return len(data)+1-2*(len(data)+1)
    return ind