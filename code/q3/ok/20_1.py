from collections import Counter

def min_freq(lst):
    # Check for decimal integers in the input list
    if any(x != int(x) for x in lst):
        return "Invalid input: Decimal integers are not allowed"

    # Calculate the frequency of each element
    element_frequency = Counter(lst)

    # Find the minimum frequency
    min_frequency = min(element_frequency.values(), default=0)

    # Find the elements with the minimum frequency
    min_frequency_elements = [element for element, frequency in element_frequency.items() if frequency == min_frequency]

    # Select the minimum element among those with the minimum frequency
    min_element = min(min_frequency_elements, default=None)

    return min_element