"""
Problem 5: Write a function reorder() that takes two arguments: a list of numbers and another number. Your function should return a list in which the numbers that are smaller than the given number appear before the numbers that are larger than the given number.

https://codecheck.io/files/23052009254fsf3krf2kbaao8g69hezp1xw
"""

from submission import reorder
from hypothesis import given, settings, HealthCheck, strategies as st
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


def main():
    nan = float("nan")
    
    result = {
        "handle_nan": False,
        "nan_key": {
            "simplest": False,
            "inductive": False
        },
        "nan_in_list": {
            "simplest": False,
            "inductive": False
        },
        "equal_values": {
            "simplest": False,
            "inductive": False
        },
    }
    
     # nan key
    
    # simplest case
    try:
        result["nan_key"]["simplest"] = reorder([0, 1], nan) == sol([0, 1], nan)
    except:
        result["nan_key"]["simplest"] = False
    
    # inductive
    @given(st.lists(st.floats(allow_nan=False), min_size=2, max_size=5).filter(lambda x: len(set(x)) > 1)) # at least two distinct values so that order matters
    @settings(suppress_health_check=(list(HealthCheck)))
    def test_inductive_nan_key(data):
        assert reorder(data, nan) == sol(data, nan)
    
    try:
        test_inductive_nan_key()
    except:
        result["nan_key"]["inductive"] = False
        
        
    # nan in list
    
    # simplest case
    try:
        result["nan_in_list"]["simplest"] = reorder([2, nan, 0], 1) == sol([2, nan, 0], 1)
    except:
        result["nan_in_list"]["simplest"] = False
        
    # inductive
    @st.composite
    def construct(draw):
        data = draw(st.lists(st.floats(), min_size=2, max_size=5).filter(lambda x: any(math.isnan(i) for i in x)))
        key = draw(st.floats(allows_nan=False).filter(lambda x: x not in data))
        return data, key
    
    _data = st.shared(construct().map(lambda x: x[0]), key="e")
    _key = st.shared(construct().map(lambda x: x[1]), key="e")
    
    @given(_data, _key)
    @settings(suppress_health_check=(list(HealthCheck)))
    def test_inductive_nan_in_list(data, key):
        assert reorder(data, key) == sol(data, key)
        
    try:
        test_inductive_nan_in_list()
    except:
        result["nan_in_list"]["inductive"] = False
        
    # equal values
    
    # simplest case
    try:
        result["equal_values"]["simplest"] = reorder([2, 1, 0], 1) == sol([2, 1, 0], 1)
    except:
        result["equal_values"]["simplest"] = False
        
    # inductive
    @st.composite
    def construct(draw):
        data = draw(st.lists(st.floats(allow_nan=False), min_size=2, max_size=5))
        key = draw(st.sampled_from(data))
        return data, key

    _data = st.shared(construct().map(lambda x: x[0]), key="e")
    _key = st.shared(construct().map(lambda x: x[1]), key="e")
    
    @given(_data, _key)
    @settings(suppress_health_check=(list(HealthCheck)))
    def test_inductive_equal_values(data, key):
        assert reorder(data, key) == sol(data, key)
        
    try:
        test_inductive_equal_values()
    except:
        result["equal_values"]["inductive"] = False

    return result


if __name__ == "__main__":
    print(main())
