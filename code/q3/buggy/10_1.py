def min_freq(data):
    # Handle the case where the input list is empty
    if not data:
        return None  # You may choose to return a specific value or raise an exception

    # Create a dictionary to store the frequency of each integer
    freq_dict = {}
    for num in data:
        # Skip non-integer elements
        if not isinstance(num, int):
            continue

        # Update the frequency in the dictionary
        freq_dict[num] = freq_dict.get(num, 0) + 1

    # Find the integer with the minimum frequency
    min_freq_num = min(freq_dict, key=freq_dict.get)

    return min_freq_num