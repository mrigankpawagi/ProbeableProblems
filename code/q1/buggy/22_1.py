def least_positive_index(nums):
    positive_nums = [num for num in nums if num > 0]

    if positive_nums:
        min_positive = min(positive_nums)
        min_positive_index = nums.index(min_positive)

        repeating_indices = [i for i, num in enumerate(nums) if num == min_positive]

        return min_positive_index, repeating_indices
    else:
        return -1, []