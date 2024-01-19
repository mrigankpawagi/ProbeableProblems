def reorder(numbers, given_number):
    """Reorders a list such that numbers smaller than the given number appear before numbers larger than it.

    Args:
        numbers: A list of numbers.
        given_number: The number to use for comparison.

    Returns:
        The reordered list.
    """

    left = 0
    right = len(numbers) - 1

    while left < right:
        while left < right and numbers[left] < given_number:
            left += 1

        while left < right and numbers[right] >= given_number:
            right -= 1

 
        if left < right:
            numbers[left], numbers[right] = numbers[right], numbers[left]

        left += 1
        right -= 1

    return numbers