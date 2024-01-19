from collections import Counter

def min_freq(arr):
    if not arr:
        return None  # Return None if the array is empty

    # Use Counter to count the occurrences of each number in the array
    counts = Counter(arr)

    # Find the number with the minimum count
    least_appearing_number = min(counts, key=counts.get)

    return least_appearing_number