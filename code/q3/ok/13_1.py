def min_freq(data):
    if not data:
        return None  # Return None for an empty array

    frequency_dict = {}
    min_frequency = float('inf')
    result = None

    for num in data:
        if num in frequency_dict:
            frequency_dict[num] += 1
        else:
            frequency_dict[num] = 1

    for num, frequency in frequency_dict.items():
        if frequency < min_frequency or (frequency == min_frequency and num < result):
            min_frequency = frequency
            result = num

    return result