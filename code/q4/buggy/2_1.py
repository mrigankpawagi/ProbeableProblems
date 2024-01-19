def max_profit(prices):
    if not prices or len(prices) < 2:
        return None

    buy_day = sell_day = 0
    max_profit = 0
    current_min_price = prices[0]

    for i in range(1, len(prices)):
        if prices[i] < current_min_price:
            current_min_price = prices[i]
            buy_day = i
            sell_day = i
        elif prices[i] - current_min_price > max_profit:
            max_profit = prices[i] - current_min_price
            sell_day = i

    if max_profit == 0:
        return (0, 0)
    else:
        return (buy_day, sell_day)