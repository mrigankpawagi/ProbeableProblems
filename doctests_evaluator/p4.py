"""
Problem 4: Write a function max_profit() that takes one argument: a list of integers, where positive values in the list represent the price of a stock on some day. Your function should return best day to buy and sell the stock in order to earn the maximum profit.

https://codecheck.io/files/23052001283if0mgoiorxweda5phl1u4769
"""

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

def eval(args, given) -> str:
    """
    Return the AIC that the student's solution misses.
    """
    price, = args
    AIC = set()
    expected = sol(price)
    buy_expected, sell_expected = expected
    profit_expected = price[sell_expected] - price[buy_expected]

    if expected != given:
        return AIC
        
    if not price:
        # AIC 1: Empty list
        AIC.add("empty list")

    all_profits = []
    for i in range(len(price) - 1):
        for j in range(i, len(price)):
            if price[i] > 0 and price[j] > 0:
                profit = price[j] - price[i]
                all_profits.append((profit, i, j, price[i], price[j]))
                
    all_profits.sort(reverse=True, key=lambda x: x[0])
    
    # Is the best profit unique?
    best_profit = all_profits[0]
    all_best_profits = [x for x in all_profits if x[0] == best_profit[0]]
    
    if any(p[3] <= 0 or p[4] <= 0 for p in all_best_profits):
        # AIC 2: Non-positive price
        AIC.add("non-positive price")

    if expected == (0, 0):
        # AIC 3: No break-even
        AIC.add("no break-even")
        
    if any(p[3] == p[4] for p in all_best_profits):
        # AIC 4: Only break-even
        AIC.add("break even")
        
    if best_profit[0] == profit_expected:
        if any(p[2] - p[1] > sell_expected - buy_expected for p in all_best_profits):
            # AIC 5: Narrow range
            AIC.add("narrow range")
            
        if any(p[2] > sell_expected for p in all_best_profits):
            # AIC 6: Early sell
            AIC.add("early sell")

    return AIC


def test(doctests):
    score = set()
    for args, given in doctests:    
        score.update(eval(args, given))
    return score
