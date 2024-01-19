import re

def first_positive_integer(s):
    # Use regular expression to find all integers in the string
    integers = re.findall(r'\b\d+\b', s)

    # Iterate through the list of integers and find the first positive one
    for num in integers:
        if int(num) > 0:
            return int(num)

    # Return None if no positive integer is found
    return None