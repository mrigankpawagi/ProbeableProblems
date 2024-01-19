def min_freq(data):
    # Create a dictionary to store the frequency of each integer
    freq_dict = {}

    # Count the frequency of each integer in the list
    for num in data:
        freq_dict[num] = freq_dict.get(num, 0) + 1

    # Find the minimum frequency among all integers
    min_frequency = min(freq_dict.values())

    # Find the smallest integer with the minimum frequency
    min_freq_num = min(num for num, freq in freq_dict.items() if freq == min_frequency)

    return min_freq_num