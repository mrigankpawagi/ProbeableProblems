def first_positive_integer(input_string):
    current_digit = ''
    has_positive_integer = False

    for char in input_string:
        if char.isdigit():
            current_digit += char
        elif current_digit:
            num = int(current_digit)
            if num > 0:
                return num
            current_digit = ''

    if current_digit:
        num = int(current_digit)
        if num > 0:
            return num

    return 0