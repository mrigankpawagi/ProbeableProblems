"""
Write a function min_freq() that takes one argument: a non-empty list of integers. Your function should return the integer that appears least often in the list.

https://codecheck.io/files/23061110151rresbylu6oa8y2va3dxdesx9
"""

from submission import min_freq
from hypothesis import given, settings, HealthCheck, strategies as st

def sol(data: list[int]) -> int:
    result = data[0]
    result_count = data.count(result)
    for n in data[1:]:
        c = data.count(n)
        if c < result_count or (c == result_count and n < result):
            result = n
            result_count = c
    return result


def main():
    result = {
        "break_ties_integer": {
            "simplest": True,
            "inductive": True
        }
    }
    
    # "the integer" (how do we break ties?)
    
    # simplest case
    try:
        result["break_ties_integer"]["simplest"] = min_freq([1, 0]) == sol([1, 0])
        # I took [1, 0] instead of [0, 1] since in the latter, one may have assumed that we are selecting 
        # the smallest integer at the smallest index
    except:
        result["break_ties_integer"]["simplest"] = False
    
    # inductive
    @given(st.lists(st.integers(min_value=-10, max_value=10), min_size=2, max_size=5).filter(lambda x: sum(sol(x) == x.count(n) for n in set(x)) > 1))
    @settings(suppress_health_check=(HealthCheck.all()))
    def test_inductive_break_ties(data):
        assert min_freq(data) == sol(data)
    
    try:
        test_inductive_break_ties()
    except:
        result["break_ties_integer"]["inductive"] = False    
        
    return result

print(main())
