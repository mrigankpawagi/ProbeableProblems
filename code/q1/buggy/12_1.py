def least_positive_index(nums):
    smallest_positive = float('inf')
    smallest_index = (len(nums)+1)*(-1)
    
    for i, num in enumerate(nums):
        if num > 0 and num < smallest_positive:
            smallest_positive = num
            smallest_index = i
    
    return smallest_index