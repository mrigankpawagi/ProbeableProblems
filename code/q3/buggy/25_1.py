def min_freq(lst):
    frequency_dict = {}
    
    for element in lst:
        if element in frequency_dict:
            frequency_dict[element] += 1
        else:
            frequency_dict[element] = 1
    
    least_frequent = min(frequency_dict, key=frequency_dict.get, default=lst[0])
    
    return least_frequent