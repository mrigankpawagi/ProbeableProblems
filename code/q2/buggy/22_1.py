def first_positive_integer(s):
    s = s.replace(" ", "")
    num_str = ""
    for char in s:
        if char.isdigit():
            num_str += char
        elif num_str:
            num = int(num_str)
            if num > 0:
                return num
            num_str = ""
    if num_str:
        num = int(num_str)
        if num > 0:
            return num
    return -1