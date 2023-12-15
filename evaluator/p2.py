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

def eval(s: str) -> str:
    """
    Return the AIC that the student's solution misses.
    """    
    expected = sol(s)
    actual = first_positive_integer(s)
    
    flag = False
    s = s.split()
    for num in s:
        if '1' <= num[0] <= '9':
            result = int(num[0])
            for d in num[1:]:
                if '0' <= d <= '9':
                    result = 10 * result + int(d)
                else:
                    break
            
            # AIC 2: Number is suffixed by non-digits
            if not num[-1].isdigit():
                if expected != actual:
                    return "suffix"
            
            # AIC 3: Number is prefixed by non-digits or '0'
            if not num[0].isdigit() or num[0] == '0':
                if expected != actual:
                    return "prefix"                

            flag = True
            break
    if not flag:
        # AIC 1: No positive integer in string
        if actual != 0:
            return "no positive"
        
score = set()

@given(st.text(alphabet="ab0-123"))
@settings(max_examples=1000)
def test(s: str):
    global score
    AIC = eval(s)
    if AIC:
        score.add(AIC)

test()
print(len(score))
