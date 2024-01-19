#Write a function, min_freq(data). Which will take a list as a input and will return the element with the least frequency. If two or more elements has the same minimum frequency then it will return the smallest elements

def min_freq(data):
    # Calculate the frequency of each element using a dictionary
    frequency_dict = {}
    for element in data:
        frequency_dict[element] = frequency_dict.get(element, 0) + 1
   
    # Find the minimum frequency
    min_frequency = min(frequency_dict.values(), default=0)
   
    # Find the elements with the minimum frequency
    min_frequency_elements = [key for key, value in frequency_dict.items() if value == min_frequency]
   
    # Return the smallest element among those with the minimum frequency
    return min(min_frequency_elements, default=None)