import re

def first_positive_integer(s):
    # Use regular expression to find all integers in the string
    integers = re.findall(r'\b\d+\b', s)

    # Iterate through the integers and find the first positive one
    for integer in integers:
        if int(integer) > 0:
            return int(integer)

    # If no positive integer is found, return None
    return None