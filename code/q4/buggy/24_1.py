def max_profit(prices):
    n = len(prices)
    
    if n < 2:
        return "Not enough days to make a profit"

    # Initialize lists to store the best buying and selling days
    buy_day = [0] * n
    sell_day = [0] * n

    # Initialize the maximum profit
    max_profit = 0

    # Find the best selling day for each day
    for i in range(1, n):
        if prices[i] < prices[buy_day[i - 1]]:
            buy_day[i] = i
        else:
            buy_day[i] = buy_day[i - 1]

        profit = prices[i] - prices[buy_day[i]]
        if profit > max_profit:
            max_profit = profit
            sell_day[i] = i

    # Find the overall best buying and selling days
    best_buy_day = buy_day[sell_day.index(max(sell_day))]
    best_sell_day = max(sell_day)

    return "Buy on day {}, sell on day {}".format(best_buy_day + 1, best_sell_day + 1)