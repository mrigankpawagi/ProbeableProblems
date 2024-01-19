def max_profit(prices):
    if not prices or len(prices) < 2:
        return -1, -1  # Handle empty list or single-day prices

    buy_day, sell_day = 0, 1
    max_profit = prices[sell_day] - prices[buy_day]

    for i in range(1, len(prices)):
        if prices[i] < prices[buy_day]:
            buy_day = i
            sell_day = i + 1
        elif prices[i] - prices[buy_day] > max_profit:
            sell_day = i
            max_profit = prices[i] - prices[buy_day]

    if max_profit <= 0:
        return -1, -1  # No profit can be made
    else:
        return buy_day, sell_day