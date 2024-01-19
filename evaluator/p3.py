"""
Write a function min_freq() that takes one argument: a non-empty list of integers. Your function should return the integer that appears least often in the list.

https://codecheck.io/files/23061110151rresbylu6oa8y2va3dxdesx9
"""

from submission import min_freq
from hypothesis import given, settings, strategies as st, example

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
        least_freq = data.count(expected)
        num_with_least_freq = sum(data.count(n) == least_freq for n in set(data))
        if num_with_least_freq > 1:
            # AIC 1: More than one least frequent number
            AIC.add("multiple least frequent")

        if not AIC:
            AIC.add("unknown")
    
    return AIC

score = set()

@example(data=[-76])
@example(data=[-1, -1])
@example(data=[2, 1, 2, 1])
@example(data=[1, 2, 1, 2])
@settings(max_examples=1000)
@given(st.lists(st.integers(min_value=-10, max_value=10), min_size=1, max_size=7))
def test(data: list[int]):
    global score
    try:
        score.update(eval(data))
    except:
        pass

test()
print(len(score))
