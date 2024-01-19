import re

def first_positive_integer(s):
    if not s:  # Check if the string is empty
        return 0

    pattern = r'\b(?:0|-\d+|[1-9]\d*)\b'  # Updated pattern to match all integers (positive, negative, and zero)
    matches = re.findall(pattern, s)
    
    for match in matches:
        num = int(match)
        if num > 0:
            return num  # Return the first positive integer found
    
    return 0  # Return 0 if no positive integer is found