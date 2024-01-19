def least_positive_index(lst):
    if not lst:
        return -1

    if any(isinstance(num, float) for num in lst):
        raise ValueError("Input array contains float numbers")

    smallest_positive = float('inf')
    for i, num in enumerate(lst):
        if num > 0 and num < smallest_positive:
            smallest_positive = num

    if smallest_positive == float('inf'):
        return -(len(lst) + 1)
    else:
        return lst.index(smallest_positive)