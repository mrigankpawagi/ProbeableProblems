def least_positive_index(data):
    # Filter positive numbers
    positive_numbers = [num for num in data if num > 0]

    if not positive_numbers:
        # If all numbers are negative, return -(n+1)
        return -(len(data) + 1)
   
    # Return the index of the minimum positive number
    return data.index(min(positive_numbers))