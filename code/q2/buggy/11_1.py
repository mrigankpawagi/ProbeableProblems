import re

def first_positive_integer(s):
    # Find all numbers in the string
    numbers = re.findall(r'-?\d+', s)
    
    # Separate positive and negative integers
    positive_integers = [int(num) for num in numbers if int(num) > 0 and ('-' + str(int(num))) not in s]
    negative_integers = [int(num) for num in numbers if int(num) < 0]
    
    # Find the positive integer occurring first
    if positive_integers:
        return positive_integers[0]
    else:
        return 0