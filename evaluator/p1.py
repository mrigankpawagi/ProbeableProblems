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

def _eval(data: list[int]) -> set[str]:
    """
    Return the AIC that the student's solution misses.
    """
    AIC = set()
    expected = sol(data)
    actual = least_positive_index(data)

    if expected != actual:
        # AIC 1a: no positive integer in list (empty list)
        if not data:
            AIC.add("empty list")

        # AIC 1b: no positive integer in list (non-empty list)
        if data and all(n <= 0 for n in data):
            AIC.add("no positive")
            
        # AIC 2: smallest positive integer appears more than once
        if any(n > 0 for n in data) and data.count(min(n for n in data if n > 0)) > 1:
            AIC.add("repeated smallest")

        if not AIC:
            AIC.add("unknown")

    return AIC
        
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
    
    # "the largest index"
    
    # simplest case
    result["largest_index"]["simplest"] = least_positive_index([1, 1]) == sol([1, 1])
    
    # inductive
    @given(st.lists(st.integers(min_value=-10, max_value=10), max_size=5).filter(lambda x: any(n > 0 for n in x) and (x.count(min(n for n in x if n > 0)) > 1)))
    @settings(suppress_health_check=(HealthCheck.all()))
    def test_inductive_largest_index(data):
        assert least_positive_index(data) == sol(data)
    
    try:
        test_inductive_largest_index()
    except:
        result["largest_index"]["inductive"] = False    
        
    # "no positive integer"
    
    # simplest case
    result["no_positive"]["simplest"] = least_positive_index([]) == sol([])
    
    # inductive
    @given(st.lists(st.integers(min_value=-10, max_value=0), max_size=5).filter(lambda x: not (any(n > 0 for n in x) and (x.count(min(n for n in x if n > 0)) > 1))))
    @settings(suppress_health_check=(HealthCheck.all()))
    def test_inductive_no_positive(data):
        assert least_positive_index(data) == sol(data)
        
    try:
        test_inductive_no_positive()
    except:
        result["no_positive"]["inductive"] = False
        
    return result
