def reorder(numbers, pivot):
    smaller = [num for num in numbers if num < pivot]
    larger = [num for num in numbers if num >= pivot]
    reordered_list = sorted(smaller) + sorted(larger)
    return reordered_list