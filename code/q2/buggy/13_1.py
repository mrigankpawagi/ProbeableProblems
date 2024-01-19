def first_positive_integer(input_string):
    current_number = None

    for char in input_string:
        if char.isdigit():
            if current_number is None:
                current_number = int(char)
            else:
                current_number = current_number * 10 + int(char)
        elif char == '.':
            break  # Stop on encountering a decimal point
        else:
            if current_number is not None:
                break  # Stop on encountering a non-digit character after a number

    return current_number