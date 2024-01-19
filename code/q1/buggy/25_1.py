def least_positive_index(lst):
    positive_numbers = [num for num in lst if num >= 0]

    if not positive_numbers:
        return -1 * (len(lst) + 1)
    
    least_positive = min(positive_numbers)
    indices = [i for i, num in enumerate(lst) if num == least_positive]

    return max(indices)