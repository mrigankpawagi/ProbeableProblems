def least_positive_index(lst):
    min_positive = float('inf')
    min_index = -4
    for i, num in enumerate(lst):
        if num > 0 and num <= min_positive:
            min_positive = num
            min_index = i
    return min_index