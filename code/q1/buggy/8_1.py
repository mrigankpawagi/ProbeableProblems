def least_positive_index(nums):
    # Filter positive integers
    positive_nums = [num for num in nums if num > 0]
    
    if positive_nums:
        # Return the index of the minimum positive integer
        return nums.index(min(positive_nums))
    else:
        # If there are no positive integers, return -2 or handle as needed
        return -2