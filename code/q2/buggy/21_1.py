import re
import math

def first_positive_integer(input_string):
    # Use regular expression to find all numbers in the string
    matches = re.findall(r'(-?\d+(\.\d+)?)', input_string)
    
    # Iterate through the matches and find the first positive integer
    for match, decimal_part in matches:
        num = float(match)
        if num > 0:
            return math.floor(num) if decimal_part else int(num)
    
    # Return None if no positive integer is found
    return None