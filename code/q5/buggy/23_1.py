def reorder(data, num):
    # Create two lists to store numbers smaller and larger than the given number
    smaller_than_num = [x for x in data if x < num]
    larger_than_num = [x for x in data if x >= num]

    # Concatenate the two lists to get the final reordered list
    reordered_list = smaller_than_num + larger_than_num

    return reordered_list