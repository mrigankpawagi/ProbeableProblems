def least_positive_index(data):
    min_positive = float('inf')
    min_index = -1
    for i, num in enumerate(data):
        if num > 0 and num <= min_positive:
            min_positive = num
            min_index = i
    return min_index