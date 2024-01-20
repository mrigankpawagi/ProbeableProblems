"""
Write a function min_freq() that takes one argument: a non-empty list of integers. Your function should return the integer that appears least often in the list.

https://codecheck.io/files/23061110151rresbylu6oa8y2va3dxdesx9
"""

def sol(data: list[int]) -> int:
    result = data[0]
    result_count = data.count(result)
    for n in data[1:]:
        c = data.count(n)
        if c < result_count or (c == result_count and n < result):
            result = n
            result_count = c
    return result

def eval(args, given) -> set[str]:
    """
    Return the AIC that the student's solution misses.
    """
    data, = args
    AIC = set()
    expected = sol(data)

    if expected != given:
        return AIC
    
    # AIC 1: More than one integer appears least often
    least_freq = data.count(expected)
    num_with_least_freq = sum(data.count(n) == least_freq for n in set(data))
    if num_with_least_freq > 1:
        # AIC 1: More than one least frequent number
        AIC.add("multiple least frequent")

    return AIC


def test(doctests):
    score = set()
    for args, given in doctests:    
        score.update(eval(args, given))
    return sorted(list(score))
