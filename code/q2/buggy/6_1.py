import re
def first_positive_integer(s):
    # Use regular expression to find all standalone numbers in the string
    # This includes numbers at the start of the string even if followed by letters
    # But excludes numbers that are part of words if the number is not at the beginning
    numbers = re.findall(r'(?<!\S)(?:-?\d+(?:\.\d+)?)(?!\S)|^\d+', s.replace(',', ''))

    # Iterate over the found numbers
    for num in numbers:
        # Convert the string to a float and then to an integer
        value = int(float(num))
        # Check if the number is positive
        if value > 0:
            return value

    # Return 0 if no positive integer is found
    return 0