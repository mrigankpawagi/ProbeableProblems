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

def eval(data: list[int]) -> str:
    """
    Return the AIC that the student's solution misses.
    """
    expected = sol(data)
    actual = min_freq(data)
    
    # AIC 1: More than one integer appears least often
    least_freq = min(data.count(n) for n in set(data))
    nums_with_least_freq = [n for n in set(data) if data.count(n) == least_freq]
    if len(nums_with_least_freq) > 1:
        if expected != actual:
            return "multiple least"

score = set()

@given(st.lists(st.integers()))
@settings(max_examples=1000)
def test(data: list[int]):
    global score
    AIC = eval(data)
    if AIC:
        score.add(AIC)

test()
print(len(score))
