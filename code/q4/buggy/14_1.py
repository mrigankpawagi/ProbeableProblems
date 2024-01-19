def max_profit(prices):
    if not prices or len(prices) < 2:
        return None
    
    buy_day = sell_day = 0
    max_profit = 0
    current_min = prices[0]

    for i in range(1, len(prices)):
        if prices[i] < current_min:
            current_min = prices[i]
            buy_day = i
        elif prices[i] - current_min > max_profit:
            max_profit = prices[i] - current_min
            sell_day = i

    return buy_day, sell_day