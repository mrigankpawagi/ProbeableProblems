def reorder(numbers, target):
    smaller_than_target = [num for num in numbers if num < target]
    larger_than_target = [num for num in numbers if num >= target]

    return smaller_than_target + larger_than_target