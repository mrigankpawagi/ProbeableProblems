import re

def first_positive_integer(s):
    # Extract numeric values using regular expression
    numbers = re.findall(r'[-+]?\d*\.\d+|\d+', s)

    # Filter positive integers
    positive_integers = [int(num) for num in numbers if int(num) > 0]

    if positive_integers:
        # Return the first positive integer
        return positive_integers[0]
    else:
        # Return 0 if there are no positive integers
        return 0