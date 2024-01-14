"""
Write a function first_positive_integer() that takes one agument: a string. Your function should return the first positive integer in the string.

https://codecheck.io/files/2306111051595nfjvjxiu7a73md5cn4saj9
"""

import re

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

def eval(args, given) -> set[str]:
    """
    Return the AIC that the student's solution misses.
    """
    s, = args
    AIC = set()
    expected = sol(s)

    if expected != given:
        return AIC
    
    # AIC 1: No positive digits
    if all(d not in '123456789' for d in s):
        AIC.add("no positive")
    else:
        expected_str = str(expected)
        i = s.index(expected_str)
        s_no_prefix = s[i:]
        s_no_suffix = s[:i + len(expected_str)]

        # AIC 2: there are integers with non-whitespace, non-digit (except 0) character in prefix
        if re.search(r"[^\s1-9][1-9]\d*", s):
            AIC.add("suffix")        

        # AIC 3: there are integers with non-whitespace character in suffix
        if re.search(r"[1-9]\d*[^\s0-9]", s):
            AIC.add("prefix")
        
        # AIC 4: More than one digit in expected
        if len(expected_str) > 1:
            AIC.add("multi digit")

    return AIC       
        
score = set()

def test(doctests):
    global score
    for args, given in doctests:    
        score.update(eval(args, given))
