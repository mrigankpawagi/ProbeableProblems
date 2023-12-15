"""
Problem 5: Write a function reorder() that takes two arguments: a list of numbers and another number. Your function should return a list in which the numbers that are smaller than the given number appear before the numbers that are larger than the given number.

https://codecheck.io/files/23052009254fsf3krf2kbaao8g69hezp1xw
"""

from submission import reorder
from hypothesis import given, settings, strategies as st
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

def eval(data: list, key) -> str:
    """
    Return the AIC that the student's solution misses.
    """
    AIC = set()
    expected = sol(data, key)
    actual = reorder(data, key)

    # AIC 1: key is NaN
    if math.isnan(key):
        if expected != actual: AIC.add("nan key")
    
    # AIC 2: Key is smaller than all numbers in list or bigger than all numbers in list
    if key < min(data) or key > max(data):
        if expected != actual: AIC.add("outside")
    
    # AIC 3: Ordering if key is between the smallest and largest number in list but not in list
    if min(data) < key < max(data) and key not in data:
        if expected != actual: AIC.add("not in list")
    
    # AIC 4: Ordering if key appears more than once in list
    if data.count(key) > 1:
        if expected != actual: AIC.add("repeated key")
    
    # AIC 5: NaN is in list
    if any(math.isnan(x) for x in data):
        if expected != actual: AIC.add("nan in list")
        
    return AIC

score = set()

@given(st.lists(st.floats() | st.integers()), st.floats() | st.integers())
@settings(max_examples=1000)
def test(data: list, key):
    global score
    score.update(eval(data, key))

test()
print(len(score))
