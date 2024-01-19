def min_freq(numbers):
    # Create a dictionary to store the frequency of each number
    freq_dict = {}
    
    # Populate the frequency dictionary
    for num in numbers:
        if num in freq_dict:
            freq_dict[num] += 1
        else:
            freq_dict[num] = 1
    
    # Find the minimum frequency
    min_frequency = min(freq_dict.values())
    
    # Find the smallest number with the minimum frequency
    min_freq_number = min(num for num, freq in freq_dict.items() if freq == min_frequency)
    
    return min_freq_number