import re

def first_positive_integer(s):
    matches = re.findall(r'(?<![\w-])(\d+)', s)
    
    for match in matches:
        if int(match) > 0:
            return int(match)
    
    return 0