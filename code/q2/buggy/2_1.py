import re

def first_positive_integer(s):
    # Extract all integers (including decimal numbers) from the string
    numbers = re.findall(r'-?\d+(\.\d+)?', s)

    # Find the first positive integer
    for number in numbers:
        num_float = float(number)
        if num_float.is_integer() and num_float > 0:
            return int(num_float)

    # Return 0 if no positive integer is found
    return 0