def min_freq(lst):
    # Create a dictionary to store the frequency and index of each integer
    freq_dict = {}
    index_dict = {}
    
    # Iterate through the list to calculate frequency and store the index of the first occurrence
    for i, num in enumerate(lst):
        freq_dict[num] = freq_dict.get(num, 0) + 1
        if num not in index_dict:
            index_dict[num] = i
    
    # Find the integer with the minimum frequency and the smallest value in case of a tie
    min_freq_num = min(freq_dict, key=lambda x: (freq_dict[x], x))
    
    return min_freq_num