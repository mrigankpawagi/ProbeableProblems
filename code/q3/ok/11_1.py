from collections import Counter

def min_freq(numbers):
    freq = Counter(numbers)
    min_freq = min(freq.values())
    numbers_with_min_freq = [num for num, f in freq.items() if f == min_freq]
    return min(numbers_with_min_freq)