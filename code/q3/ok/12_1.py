from collections import Counter

def min_freq(nums):
    count = Counter(nums)
    min_frequency = min(count.values())
    least_frequent = [num for num, freq in count.items() if freq == min_frequency]
    return min(least_frequent)