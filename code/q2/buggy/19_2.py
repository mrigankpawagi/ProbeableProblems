import re
def first_positive_integer(s):
    # Extract all integers (positive and negative) from the string
    integers = re.findall(r'-?\d+', s)

    if not integers:
        # If no integers are found, return 0
        return 0
   
    # Iterate through the integers to find the first positive one
    for num in integers:
        if int(num) > 0:
            return int(num)
   
    # If no positive integers are found, return 0
    return 0