"""
Problem 4: Write a function max_profit() that takes one argument: a list of integers, where positive values in the list represent the price of a stock on some day. Your function should return best day to buy and sell the stock in order to earn the maximum profit.

https://codecheck.io/files/23052001283if0mgoiorxweda5phl1u4769
"""

from submission import max_profit
from hypothesis import given, settings, strategies as st

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

def eval(price: list[int]) -> str:
    """
    Return the AIC that the student's solution misses.
    """
    AIC = set()
    expected = sol(price)
    actual = max_profit(price)

    if expected != actual:
        if not price:
            # AIC 1: Empty list
            AIC.add("empty list")
        elif not isinstance(actual, tuple) or len(actual) != 2:
            AIC.add("unknown")
        else:
            buy_expected, sell_expected = expected
            buy_actual, sell_actual = actual
            if buy_actual < 0 or buy_actual > sell_actual or sell_actual >= len(price) or\
            price[sell_actual] - price[buy_actual] < price[sell_expected] - price[buy_expected]:
                AIC.add("unknown")
            else:
                if price[buy_actual] <= 0 or price[sell_actual] <= 0:
                    # AIC 2: Positive price
                    AIC.add("positive price")
                elif expected == (0, 0):
                    # AIC 3: No profit
                    AIC.add("no profit")
                else:
                    if sell_actual - buy_actual > sell_expected - buy_expected:
                        # AIC 4: Narrow range
                        AIC.add("narrow range")
                    if sell_actual > sell_expected:
                        # AIC 5: Early sell
                        AIC.add("early sell")

    return AIC

score = set()

@given(st.lists(st.integers(), max_size=7))
@settings(max_examples=1000)
def test(price: list[int]):
    global score
    score.update(eval(price))

test()
print(len(score))
