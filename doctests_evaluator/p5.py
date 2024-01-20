"""
Problem 5: Write a function reorder() that takes two arguments: a list of numbers and another number. Your function should return a list in which the numbers that are smaller than the given number appear before the numbers that are larger than the given number.

https://codecheck.io/files/23052009254fsf3krf2kbaao8g69hezp1xw
"""

import math

def sol(data: list, key) -> list:
    if math.isnan(key):
        return data
    lo = [x for x in data if x < key]
    hi = [x for x in data if x > key]
    result = []
    lo_index = 0
    hi_index = 0
    for i in range(len(data)):
        if math.isnan(data[i]) or data[i] == key:
            result.append(data[i])
        elif lo_index < len(lo):
            result.append(lo[lo_index])
            lo_index += 1
        else:
            result.append(hi[hi_index])
            hi_index += 1
    return result

def eval(args, given) -> str:
    """
    Return the AIC that the student's solution misses.
    """
    data, key = args
    AIC = set()
    expected = sol(data, key)

    if expected != given:
        return AIC
    
    if math.isnan(key):
        # AIC 1: key is nan
        AIC.add("nan key")
    else:
        expected_filtered = [x for x in expected if not math.isnan(x) and x != key]
        given_filtered = [x for x in data if not math.isnan(x) and x != key]
        
        num_small = sum(x < key for x in expected_filtered)
        
        if expected_filtered[:num_small] != given_filtered[:num_small] or \
            expected_filtered[num_small:] != given_filtered[num_small:]:
            # AIC 2: Order of elements
            AIC.add("order")
            
        if any(math.isnan(x) for x in data):
            # AIC 3: Position of nan in result
            AIC.add("nan position")
            
        if key in data:
            # AIC 4: Position of key in result
            AIC.add("key position")
        
    return AIC


def test(doctests):
    score = set()
    for args, given in doctests:    
        try:
            score.update(eval(args, given))
        except:
            pass
    return sorted(list(score))
