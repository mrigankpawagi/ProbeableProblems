"""
Problem 4: Write a function max_profit() that takes one argument: a list of integers, where positive values in the list represent the price of a stock on some day. Your function should return best day to buy and sell the stock in order to earn the maximum profit.

https://codecheck.io/files/23052001283if0mgoiorxweda5phl1u4769
"""

from submission import max_profit
from hypothesis import given, settings, strategies as st, example

def sol(price: list[int]) -> tuple[int, int] | None:
    if not price:
        return None
    max_profit = None
    best_buy = None
    best_sell = None
    for i in range(len(price) - 1):
        for j in range(i + 1, len(price)):
            if price[i] > 0 and price[j] > 0:
                profit = price[j] - price[i]
                if profit >= 0:
                    if max_profit is None or profit > max_profit:
                        max_profit = profit
                        best_buy = i
                        best_sell = j
                    elif profit == max_profit:
                        if (j - i < best_sell - best_buy) or (j - i == best_sell - best_buy and j < best_sell):
                            best_buy = i
                            best_sell = j
    if max_profit is None:
        return (0, 0)
    return best_buy, best_sell


def main():
    result = {
        "empty_list_none": True,
        "return_type_tuple": True,
        "negative_profit": True,
        "sell_after_buy": True,
        "no_profit": True,
        "zero_profit": True,
        "ignore_non_positive": True,
        "tie_break": True,
        "residue": True,       
    }


    def check(data, bug: str):
        try:
            res = max_profit(data)
            if not isinstance(res, tuple) and data != []:
                res = tuple(res)
            
            assert res == sol(data)
        except:
            result[bug] = False
            
    # empty list
    try:
        assert max_profit([]) == None
    except:
        result["empty_list_none"] = False
        
    
    def simple():
        # Return a list of >= 2 unique
        # integers in ascending order,
        # with unique gaps between them
        # to avoid tie-breaking.
        return st.lists(
            st.integers(min_value=0, max_value=10),
            min_size=2, max_size=5, unique=True
        ).map(lambda x: [2 ** i for i in sorted(x)])
        
    # return_type_tuple
    @given(simple())
    def return_type_tuple(data):
        try:
            res = max_profit(data[:])
            assert isinstance(res, tuple) and len(res) == 2
        except:
            result["return_type_tuple"] = False
            
    return_type_tuple()
            
    
    # non negative profit sell and buy
    @given(simple())
    def nonneg_profit_sell_after_buy(data):
        try:
            t = max_profit(data[:])
            assert data[t[1]] >= data[t[0]]
        except:
            result["negative_profit"] = False

        try:
            assert t[0] < t[1]
        except:
            result["sell_after_buy"] = False
            
    nonneg_profit_sell_after_buy()


    @given(simple())
    def no_profit(data):
        data = data[::-1]
        check(data, "no_profit")


    @given(simple(), st.integers(min_value=0, max_value=4))
    def zero_profit(data, i):
        i = i % len(data)
        data = data[:i] + [data[i]] + data[i:]
        check(data[::-1], "zero_profit")


    @given(simple(), st.integers(min_value=0, max_value=4))
    def ignore_non_positive(data, i):
        random_element = data[i % len(data)]
        data = [random_element - x for x in data[::-1]]
        check(data, "ignore_non_positive")


    @given(st.lists(st.integers(min_value=1, max_value=10), min_size=4, max_size=6))
    def tie_break(data):
        check(data, "tie_break")


    @given(st.lists(st.integers(min_value=-5, max_value=10), max_size=6))
    def check_all(data):
        check(data, "residue")
        
    no_profit()
    zero_profit()
    ignore_non_positive()
    tie_break()
    check_all()
  
    return result


if __name__ == "__main__":
    print(main())
