import re

def first_positive_integer(s):
    # Use regular expression to find all integer matches in the string
    matches = re.findall(r'\b\d+\b', s)

    for match in matches:
        number = int(match)
        if number > 0:
            return number

    return None