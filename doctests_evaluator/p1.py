"""
Write a function least_positive_index() that takes one argument: a list of integers. Your function should return the index of the smallest positive integer in the list.

https://codecheck.io/files/2306111033cnnmzafkxveg0ap6i7blj01f0
"""

def sol(data: list[int]) -> int:
    result = -(len(data) + 1)
    for i, n in enumerate(data):
        if n > 0 and (result < 0 or 0 < n <= data[result]):
            result = i
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
    
    # AIC 1a: no positive integer in list (empty list)
    if not data:
        AIC.add("empty list")

    # AIC 1b: no positive integer in list (non-empty list)
    if data and all(n <= 0 for n in data):
        AIC.add("no positive")
        
    # AIC 2: smallest positive integer appears more than once
    if any(n > 0 for n in data) and data.count(min(n for n in data if n > 0)) > 1:
        AIC.add("repeated smallest")

    return AIC


def test(doctests):
    score = set()
    for args, given in doctests:    
        score.update(eval(args, given))
    return score
