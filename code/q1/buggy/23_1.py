def least_positive_index(nums):
    # Filter positive integers
    positive_numbers = [num for num in nums if num > 0]

    if not positive_numbers:
        # If there are no positive integers, return None
        return None

    # Find the index of the minimum positive integer
    min_positive_index = nums.index(min(positive_numbers))

    return min_positive_index