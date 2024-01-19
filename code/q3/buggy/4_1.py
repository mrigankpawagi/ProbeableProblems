def min_freq(lst):
    # Create a dictionary to store the frequency of each element
    freq_dict = {}

    # Iterate through the list and update the frequency dictionary
    for elem in lst:
        if elem in freq_dict:
            freq_dict[elem] += 1
        else:
            freq_dict[elem] = 1

    # Find the element with the minimum frequency and minimum index
    min_freq_elem = min(lst, key=lambda x: (freq_dict[x], lst.index(x)))

    return min_freq_elem