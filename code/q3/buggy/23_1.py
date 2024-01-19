def min_freq(lst):
    # Create a dictionary to store the frequency of each integer
    freq_dict = {}
    
    # Count the frequency of each integer in the list
    for num in lst:
        if num in freq_dict:
            freq_dict[num] += 1
        else:
            freq_dict[num] = 1
    
    # Find the minimum frequency and corresponding integer
    min_freq = float('inf')  # Initialize min_freq to positive infinity
    min_freq_num = None
    
    for num, freq in freq_dict.items():
        if freq < min_freq:
            min_freq = freq
            min_freq_num = num
    
    return min_freq_num