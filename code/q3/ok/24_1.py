def min_freq(data):
    # Create a dictionary to store the frequency of each integer in the list
    freq_dict = {}

    # Count the frequency of each integer in the list
    for num in data:
        freq_dict[num] = freq_dict.get(num, 0) + 1

    # Find the integers with the minimum frequency
    min_freq_nums = [num for num, freq in freq_dict.items() if freq == min(freq_dict.values())]

    # If there are multiple integers with the minimum frequency, return the smallest one
    return min(min_freq_nums)