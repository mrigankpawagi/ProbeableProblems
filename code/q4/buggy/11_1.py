def max_profit(prices):
    if not prices or len(prices) < 2:
        return [0, 0]

    buy_day = 0
    sell_day = 0
    max_profit = 0

    for i in range(len(prices)):
        for j in range(i + 1, len(prices)):
            profit = prices[j] - prices[i]
            if profit > max_profit:
                buy_day = i
                sell_day = j
                max_profit = profit
            elif profit == 0 and (sell_day - buy_day > j - i or max_profit == 0):
                buy_day = i
                sell_day = j

    return [buy_day, sell_day]