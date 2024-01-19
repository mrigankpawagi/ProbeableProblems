def reorder(data, num):
    if not data:
        return []  # Return an empty array if the input is empty

    # Partition the array into two parts: elements less than 'num' and elements greater than 'num'
    smaller_than_num = [x for x in data if x < num]
    greater_than_num = [x for x in data if x > num]

    # Combine the two parts to get the reordered array
    reordered_data = smaller_than_num + [num] * data.count(num) + greater_than_num

    return reordered_data