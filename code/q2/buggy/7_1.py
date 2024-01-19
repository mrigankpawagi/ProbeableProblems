import re

def first_positive_integer(s):
    # Use regular expression to find all integers in the string
    integers = re.findall(r'\b(\d+)\b', s)

    # Filter out numbers with a dot (decimal numbers) and convert to integers
    positive_integers = [int(match) for match in integers if '.' not in match and int(match) > 0]

    # Return the first positive integer or 0 if none is found
    return positive_integers[0] if positive_integers else 0