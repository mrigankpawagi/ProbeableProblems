import re

def first_positive_integer(input_string):
    # Define a regular expression pattern to match standalone positive integers
    pattern = r'\b(?:0|[1-9]\d*)\b'
    
    # Find all matches in the input string
    matches = re.findall(pattern, input_string)
    
    # Filter out negative numbers and those with symbols before the integer without spaces
    positive_numbers = [int(match) for match in matches if int(match) >= 0 and re.search(r'\b' + re.escape(match), input_string)]
    
    # Return the first positive integer (if any), or None if no positive integer is found
    return positive_numbers[0] if positive_numbers else None