def min_freq(nums):
    # Create a dictionary to store the frequency of each number
    freq_dict = {}
    
    # Count the frequency of each number in the list
    for num in nums:
        freq_dict[num] = freq_dict.get(num, 0) + 1
    
    # Find the number with the minimum frequency
    min_freq_num = min(freq_dict, key=freq_dict.get)
    
    return min_freq_num