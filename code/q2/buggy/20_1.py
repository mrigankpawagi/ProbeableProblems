import re

def first_positive_integer(s):
    # Use regular expression to find all integers in the string
    matches = re.findall(r'-?\b\d+\b', s)

    # Iterate through the matches
    for match in matches:
        num = int(match)
        # Check if the number is positive
        if num > 0:
            return num  # Return the first positive integer

    # Return None if no positive integer is found
    return None