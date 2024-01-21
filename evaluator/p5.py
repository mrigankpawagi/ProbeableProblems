"""
Problem 5: Write a function reorder() that takes two arguments: a list of numbers and another number. Your function should return a list in which the numbers that are smaller than the given number appear before the numbers that are larger than the given number.

https://codecheck.io/files/23052009254fsf3krf2kbaao8g69hezp1xw
"""

from submission import reorder
from hypothesis import given, settings, strategies as st, example
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

    if expected != actual:
        if math.isnan(key):
            # AIC 1: key is nan
            AIC.add("nan key")
        else:
            expected_filtered = [x for x in expected if not math.isnan(x) and x != key]
            actual_filtered = [x for x in actual if not math.isnan(x) and x != key]
            if expected_filtered != actual_filtered:
                num_small = sum(x < key for x in expected_filtered)
                if sorted(expected_filtered[:num_small]) == sorted(actual_filtered[:num_small]) and\
                sorted(expected_filtered[num_small:]) == sorted(actual_filtered[num_small:]):
                    # AIC 2: Order of elements
                    AIC.add("order")
            else:
                if any(math.isnan(x) for x in data):
                    # AIC 3: Position of nan in result
                    AIC.add("nan position")
                if key in data:
                    # AIC 4: Position of key in result
                    AIC.add("key position")
        if not AIC:
            AIC.add("unknown")
                
    return AIC

if __name__ == "__main__":
    import sys
    
    if len(sys.argv) > 1:
        data = eval(sys.argv[1:])
        try:
            print(sorted(eval(data)))
        except:
            pass
    
    else:
        score = set()

    @example(data=[-1, -1], key=float('nan'))
    @example(data=[5, 3.0, 2, 4, 1, 3], key=3)
    @example(data=[float('nan'), 5, float('nan'), float('nan'), 1, float('nan')], key=3)
    @example(data=[5, float('inf'), 1, 4, 2, float('inf')], key=float('inf'))
    @example(data=[5, float('-inf'), 1, 4, 2, float('-inf')], key=float('-inf'))
    @settings(max_examples=2000)
    @given(st.lists(st.floats() | st.integers(), max_size=7), st.floats() | st.integers())
    def test(data: list, key):
        global score
        try:
            score.update(eval(data, key))
        except:
            pass

    test()
    print(sorted(list(score)))
