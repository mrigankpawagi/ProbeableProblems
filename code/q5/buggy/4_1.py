def reorder(lst, num):
    if not lst:
        # Return an empty list if the input list is empty
        return []

    # Separate the numbers into two groups: smaller and larger than the given number
    smaller_than_num = [x for x in lst if x < num]
    larger_than_num = [x for x in lst if x >= num]

    # Concatenate the two groups while maintaining the original order
    result = smaller_than_num + larger_than_num

    return result