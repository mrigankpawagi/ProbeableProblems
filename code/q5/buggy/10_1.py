def reorder(data, num):
    # Handle the case where the input list is empty
    if not data:
        return []

    # Separate numbers smaller and larger than the given number
    smaller = [x for x in data if x < num]
    larger = [x for x in data if x > num]

    # Combine the two lists while preserving the order
    result = smaller + [num] * data.count(num) + larger

    return result