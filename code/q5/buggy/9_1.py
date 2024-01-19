def reorder(data, num):
    smaller_or_equal = [x for x in data if x <= num]
    larger = [x for x in data if x > num]
    return smaller_or_equal + larger