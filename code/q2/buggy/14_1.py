def first_positive_integer(s):
    """
    Returns the first positive integer in the given string.

    If no positive integer is found, returns 0.

    Example:
    >>> first_positive_integer("abc 42 def 17 xyz")
    42

    >>> first_positive_integer("No positive integers here!")
    0
    """
    for word in s.split():
        if word.isdigit() and int(word) > 0:
            return int(word)
    return 0