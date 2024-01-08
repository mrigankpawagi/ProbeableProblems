"""
Write a function min_freq() that takes one argument: a non-empty list of integers. Your function should return the integer that appears least often in the list.

https://codecheck.io/files/23061110151rresbylu6oa8y2va3dxdesx9
"""

from submission import min_freq
from hypothesis import given, settings, strategies as st

def sol(data: list[int]) -> int:
    result = data[0]
    result_count = data.count(result)
    for n in data[1:]:
        c = data.count(n)
        if c < result_count or (c == result_count and n < result):
            result = n
            result_count = c
    return result

def eval(data: list[int]) -> set[str]:
    """
    Return the AIC that the student's solution misses.
    """
    AIC = set()
    expected = sol(data)
    actual = min_freq(data)

    if expected != actual:
        # AIC 1: More than one integer appears least often
        least_freq = data.count(result)
        num_with_least_freq = sum(1 for n in set(data) if data.count(n) == least_freq)
        if num_with_least_freq > 1:
            AIC.add("multiple least frequent")
        else:
            AIC.add("unknown")
    
    return AIC

score = set()

@given(st.lists(st.integers(), min_size=1, max_size=7))
@settings(max_examples=1000)
def test(data: list[int]):
    global score
    score.update(eval(data))

test()
print(len(score))
