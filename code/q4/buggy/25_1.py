def max_profit(prices):
    if len(prices) <= 1 or all(price == prices[0] for price in prices):
        return (0, 0)

    max_profit = 0
    buy_day = 0
    sell_day = 1

    for i in range(len(prices) - 1):
        for j in range(i + 1, len(prices)):
            profit = prices[j] - prices[i]
            if profit > max_profit:
                max_profit = profit
                buy_day = i
                sell_day = j

    return (buy_day, sell_day)