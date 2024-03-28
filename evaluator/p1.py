"""
Write a function least_positive_index() that takes one argument: a list of integers. Your function should return the index of the smallest positive integer in the list.

https://codecheck.io/files/2306111033cnnmzafkxveg0ap6i7blj01f0
"""

from submission import least_positive_index
from hypothesis import given, settings, HealthCheck, strategies as st

def sol(data: list[int]) -> int:
    result = -(len(data) + 1)
    for i, n in enumerate(data):
        if n > 0 and (result < 0 or 0 < n <= data[result]):
            result = i
    return result


def main():
    result = {
        "largest_index": {
            "simplest": True,
            "inductive": True
        },
        "no_positive": {
            "simplest": True,
            "inductive": True
        }
    }
    
    # "the largest index" (but all values positive)
    
    # simplest case
    try:
        result["largest_index"]["simplest"] = least_positive_index([1, 1]) == sol([1, 1])
    except:
        result["largest_index"]["simplest"] = False
    # inductive
    @given(st.lists(st.integers(min_value=1, max_value=10), min_size=2, max_size=5).filter(lambda x: any(n > 0 for n in x) and (x.count(min(n for n in x if n > 0)) > 1)))
    @settings(suppress_health_check=(HealthCheck.all()))
    def test_inductive_largest_index(data):
        assert least_positive_index(data) == sol(data)
    
    try:
        test_inductive_largest_index()
    except:
        result["largest_index"]["inductive"] = False    
        
    # "no positive integer"
    
    # simplest case
    try:
        result["no_positive"]["simplest"] = least_positive_index([]) == sol([])
    except:
        result["no_positive"]["simplest"] = False

    # inductive
    @given(st.lists(st.integers(min_value=-10, max_value=0), min_size=1, max_size=5).filter(lambda x: (x.count(min(x)) == 1)))
    @settings(suppress_health_check=(HealthCheck.all()))
    def test_inductive_no_positive(data):
        assert least_positive_index(data) == sol(data)
        
    try:
        test_inductive_no_positive()
    except:
        result["no_positive"]["inductive"] = False
        
    return result
