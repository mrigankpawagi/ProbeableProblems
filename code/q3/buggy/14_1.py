from collections import Counter

def min_freq(nums):
    return min(Counter(nums), key=Counter(nums).get)