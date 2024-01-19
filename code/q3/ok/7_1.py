from collections import Counter

def min_freq(data):
    # Use Counter to count occurrences of each integer
    freq_counter = Counter(data)

    # Find the minimum frequency
    min_frequency = min(freq_counter.values())

    # Find the integers with the minimum frequency
    min_freq_integers = [num for num, freq in freq_counter.items() if freq == min_frequency]

    # Return the smallest integer with the minimum frequency
    return min(min_freq_integers)