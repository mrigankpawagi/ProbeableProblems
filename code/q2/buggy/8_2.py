def first_positive_integer(s):
    # Extract all integers from the string
    integers = [int(word) for word in s.split() if word.strip().isdigit()]

    # Find the first positive integer, if any
    for num in integers:
        if num > 0:
            return num

    # Return 0 if no positive integer is found, otherwise return 9
    return 0 if not integers else 9