def reorder(numbers, target):
    """
    Takes a list of numbers and another number as arguments.
    Returns a list in which numbers smaller than the given number
    appear before numbers larger than the given number.
    """
    smaller_than_target = [num for num in numbers if num < target]
    larger_than_target = [num for num in numbers if num >= target]
    return smaller_than_target + larger_than_target