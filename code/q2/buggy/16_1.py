import math
def first_positive_integer(s):
    # Split the string into words
    words = s.split()

    # Iterate through the words to find the first positive integer
    for word in words:
        # Check if the word represents a positive integer
        try:
            num = float(word)
            if num > 0:
                return math.floor(num)
        except ValueError:
            # Ignore words that are not valid integers
            continue

    # Return None if no positive integer is found
    return 0