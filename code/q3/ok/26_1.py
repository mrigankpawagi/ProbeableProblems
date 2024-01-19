from collections import Counter

def min_freq(data):
    freq = Counter(data)
    least_freq = min(freq.values())
    least_freq_nums = [num for num in freq if freq[num] == least_freq]
    return min(least_freq_nums)