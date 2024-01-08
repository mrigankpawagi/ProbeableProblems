"""
Write a function first_positive_integer() that takes one agument: a string. Your function should return the first positive integer in the string.

https://codecheck.io/files/2306111051595nfjvjxiu7a73md5cn4saj9
"""

from submission import first_positive_integer
from hypothesis import given, settings, strategies as st

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

def eval(s: str) -> set[str]:
    """
    Return the AIC that the student's solution misses.
    """
    AIC = set()
    expected = sol(s)
    actual = first_positive_integer(s)

    if expected != actual:
        # AIC 1: No positive digits
        if all(d not in '123456789' for d in s):
            AIC.add("no positive")
        else:  # AIC 1 is a special case all by itself
            expected_str = str(expected)
            i = s.index(expected_str)
            s_no_prefix = s[i:]
            s_no_suffix = s[:i + len(expected_str)]

            # AIC 2: Something in the prefix is causing a problem
            if first_positive_integer(s_no_prefix) == actual:
                AIC.add("prefix")
            # AIC 3: Something in the suffix is causing a problem
            if first_positive_integer(s_no_suffix) == actual:
                AIC.add("suffix")

            if not AIC:
                AIC.add("unknown")

    return AIC       
        
score = set()

@given(st.text(alphabet="-., b013", max_size=7))
@settings(max_examples=1000)
def test(s: str):
    global score
    score.update(eval(s))

test()
print(len(score))
