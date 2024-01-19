def min_freq(nums):
    num_counts = {}
    for num in nums:
        if num in num_counts:
            num_counts[num] += 1
        else:
            num_counts[num] = 1
    min_frequency = min(num_counts.values())
    min_freq_integers = [num for num, count in num_counts.items() if count == min_frequency]
    return tuple(min_freq_integers)