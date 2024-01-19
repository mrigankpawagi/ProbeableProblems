def reorder(nums, target):
    if not nums:
        return []

    smaller = [x for x in nums if x < target]
    larger = [x for x in nums if x >= target]

    return smaller + larger