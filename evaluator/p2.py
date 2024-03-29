"""
Write a function first_positive_integer() that takes one agument: a string. Your function should return the first positive integer in the string.

https://codecheck.io/files/2306111051595nfjvjxiu7a73md5cn4saj9
"""

from submission import first_positive_integer
from hypothesis import given, settings, HealthCheck, strategies as st

def sol(s: str) -> int:
    s = s.split()
    for num in s:
        if '1' <= num[0] <= '9':
            result = int(num[0])
            for d in num[1:]:
                if '0' <= d <= '9':
                    result = 10 * result + int(d)
                else:
                    break
            return result
    return 0  


def main():
    result = {
        "return_int": True,
        "starts_with_nonzero_digit": True,
        "longest_integer_prefix": True,
        "first_word_starts_with_nonzero": True,
        "no_integer": {
            "simplest": True,
            "inductive": True
        }, 
        "residue": True,
    }
    
    Digits = '0123456789'
    Symbols = '+-.,\t\n'


    def check(s: str, bug: str):
        try:
            res = first_positive_integer(s)
            if not isinstance(res, int):
                result["return_int"] = False
                res = int(res)
            
            assert res == sol(s)
        except:
            result[bug] = False


    def starts_with_nonzero_digit():
        check('', 'starts_with_nonzero_digit')
        check('0', 'starts_with_nonzero_digit')
        for d in Digits[1:]:
            check(d, 'starts_with_nonzero_digit')
            check('0' + d, 'starts_with_nonzero_digit')
            for s in Symbols:
                check(s + d, 'starts_with_nonzero_digit')
        for s in Symbols:
            check(s, 'starts_with_nonzero_digit')


    @given(
        st.text(alphabet=Digits[1:], min_size=1, max_size=4),
        st.text(alphabet=Digits + Symbols, min_size=0, max_size=3)
    )
    def longest_integer_prefix(s, t):
        check(s + t, 'longest_integer_prefix')


    @given(
        st.lists(st.text(alphabet=Digits + Symbols, min_size=1, max_size=1), min_size=2, max_size=5)
    )
    def first_word_starts_with_nonzero_digit(words):
        check(' '.join(words), 'first_word_starts_with_nonzero')


    @given(
        st.lists(st.text(alphabet=Digits + Symbols, min_size=1, max_size=5), min_size=0, max_size=5)
    )
    def check_all(words):
        check(' '.join(words), 'residue')
        
    starts_with_nonzero_digit()
    longest_integer_prefix()
    first_word_starts_with_nonzero_digit()
    check_all()
    
    # no integer
    
    # simplest case
    try:
        _res = first_positive_integer('')
        if not isinstance(_res, int):
            result["no_integer"]["simplest"] = False
            _res = int(_res)
            
        result["no_integer"]["simplest"] = _res == sol('')
    except:
        result["no_integer"]["simplest"] = False
        
    # inductive
    @given(
        st.text(alphabet=Digits[1:], min_size=1, max_size=4),
        st.text(alphabet=Digits[0] + Symbols, min_size=0, max_size=3)
    )
    def longest_integer_prefix(s, t):
        _res = first_positive_integer(t + s)
        if not isinstance(_res, int):
            result["no_integer"]["inductive"] = False
            _res = int(_res)
            
        assert _res == sol(t + s)
        
    try:
        longest_integer_prefix()
    except:
        result["no_integer"]["inductive"] = False
  
    return result


if __name__ == "__main__":
    print(main())
