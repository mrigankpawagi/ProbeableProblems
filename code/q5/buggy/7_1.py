def reorder(data, num):
    # Separate the numbers smaller and larger than the given number
    smaller = [x for x in data if x < num]
    larger = [x for x in data if x >= num]

    # Combine the lists to get the desired order
    result = smaller + larger

    return result