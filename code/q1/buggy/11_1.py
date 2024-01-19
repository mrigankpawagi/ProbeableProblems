def least_positive_index(numbers):
    least_positive = None
    least_positive_index = None

    for i in range(len(numbers) - 1, -1, -1):
        if numbers[i] > 0:
            if least_positive is None or numbers[i] < least_positive:
                least_positive = numbers[i]
                least_positive_index = i

    return least_positive_index if least_positive_index is not None else -1