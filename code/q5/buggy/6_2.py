def reorder(data, num):
    less_than = [x for x in data if x < num]
    greater_than_or_equal = [x for x in data if x >= num]
    return less_than + greater_than_or_equal