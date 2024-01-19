def reorder(data, num):
    return [x for x in data if x < num] + [x for x in data if x >= num]