def least_positive_index(nums):
    # Filter out negative integers and zero
    positive_nums = [num for num in nums if num > 0]

    # If there are no positive integers, return 1 (smallest positive integer)
    if not positive_nums:
        return 1

    # Sort the positive integers
    positive_nums.sort()

    # Find the least positive integer
    least_positive_integer = 1
    for num in positive_nums:
        if num == least_positive_integer:
            least_positive_integer += 1
        else:
            break

    return least_positive_integer