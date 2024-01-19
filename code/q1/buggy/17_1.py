def least_positive_index(lst):
    min_positive = float('inf')
    min_index = -1

    for i in range(len(lst) - 1, -1, -1):
        if lst[i] > 0 and lst[i] < min_positive:
            min_positive = lst[i]
            min_index = i

    return min_index