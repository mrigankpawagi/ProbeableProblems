from collections import Counter

def min_freq(arr):
    if not arr:  # Check if the list is empty
        return None

    counts = Counter(arr)
    min_count = min(counts.values())
    least_occuring = [num for num, count in counts.items() if count == min_count]

    return min(least_occuring) if least_occuring else None