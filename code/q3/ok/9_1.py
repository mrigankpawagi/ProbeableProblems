from collections import Counter

def min_freq(data):
    count = Counter(data)
    min_freq = min(count.values())
    least_freq_nums = [num for num, freq in count.items() if freq == min_freq]
    return min(least_freq_nums)