def reorder(numbers, pivot):
    # Use list comprehension to reorder the numbers
    smaller = [num for num in numbers if num < pivot]
    larger_or_equal = [num for num in numbers if num >= pivot]
    reordered_list = smaller + larger_or_equal
    return reordered_list