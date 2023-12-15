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
    AIC = set()
    expected = sol(s)
    actual = first_positive_integer(s)

    s = s.split()
    for num in s:
        if '1' <= num[0] <= '9':
            result = int(num[0])
            for d in num[1:]:
                if '0' <= d <= '9':
                    result = 10 * result + int(d)
                else:
                    break
            
            # AIC 2: First positive integer is suffixed by non-digits
            if any(not c.isdigit() for c in num):
                if expected != actual: AIC.add("suffix")
                
            flag = True
            break
    if not flag:
        # AIC 1: No positive integer in string
        if actual != 0: AIC.add("no positive")
            
    # AIC 3: First positive integer is prefixed by non-digits or '0'
    for num in s:
        digit_indices = [i for i in range(len(num)) if num[i] in '123456789']
        if digit_indices:
            first_digit_index = min(digit_indices)
            if first_digit_index > 0:
                if expected != actual: AIC.add("prefix")
            break
        
    return AIC       
        
score = set()

@given(st.text(alphabet="ab0-123"))
@settings(max_examples=1000)
def test(s: str):
    global score
    score.update(eval(s))

test()
print(len(score))
