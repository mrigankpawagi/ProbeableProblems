def first_positive_integer(s):
    # Split the string into words
    words = s.split()

    # Iterate through the words to find the first positive integer
    for word in words:
        # Remove non-numeric characters and check if the remaining string is a positive integer
        numeric_part = ''.join(char for char in word if char.isdigit())
        if numeric_part and int(numeric_part) > 0:
            return int(numeric_part)

    # If no positive integer is found, return 0
    return 0