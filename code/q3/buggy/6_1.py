def min_freq(numbers):
    # Count the frequency of each number
    frequency = {}
    for number in numbers:
        frequency[number] = frequency.get(number, 0) + 1

    # Find the number(s) with the minimum frequency
    min_freq = min(frequency.values())
    min_freq_numbers = [num for num, freq in frequency.items() if freq == min_freq]

    # Return the smallest number with minimum frequency if it's unique, otherwise None
    return min(min_freq_numbers) if len(min_freq_numbers) == 1 else None