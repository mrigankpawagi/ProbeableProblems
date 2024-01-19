import re

def first_positive_integer(s):
    numbers = re.findall(r'\b[1-9][0-9]*\b', s)
    if numbers:
        return int(numbers[0])
    return None