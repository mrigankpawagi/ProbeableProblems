def first_positive_integer(s):
    num = ''
    
    for char in s:
        if char.isdigit():
            num += char
            if num != '0' and int(num) > 0:
                return int(num)
        else:
            if num != '':
                break
    
    return 0