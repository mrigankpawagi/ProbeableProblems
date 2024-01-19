import re

def first_positive_integer(s):
    numbers = [int(num) for num in re.findall(r'\d+', s)]
    for num in numbers:
        if num > 0:
            return num
    return None