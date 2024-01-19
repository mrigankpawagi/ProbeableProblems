def max_profit(prices):
    if len(prices) < 2:
        return None

    buy_day = sell_day = 0
    max_profit = 0
    current_min = float('inf')

    for i in range(len(prices)):
        if prices[i] == 0:
            current_min = float('inf')
            continue

        if prices[i] <= current_min:
            current_min = prices[i]
            buy_day = i
            sell_day = i
        elif prices[i] - current_min > max_profit:
            max_profit = prices[i] - current_min
            sell_day = i

    return (buy_day, sell_day)