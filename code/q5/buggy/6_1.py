def reorder(numbers, pivot):
    less_than_pivot = [num for num in numbers if num < pivot]
    greater_than_pivot = [num for num in numbers if num > pivot]
    pivot_included = [num for num in numbers if num == pivot]

    return less_than_pivot + pivot_included + greater_than_pivot