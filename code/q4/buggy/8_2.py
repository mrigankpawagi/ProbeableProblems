def max_profit(price):
    if not price or len(price) < 2:
        return "Not enough data to compute profit"

    buy_day, sell_day = 0, 0
    max_profit = 0
    current_min = price[0]
    current_profit = 0

    for i in range(1, len(price)):
        if price[i] < current_min:
            current_min = price[i]
            buy_day = i

        current_profit = price[i] - current_min

        if current_profit > max_profit:
            max_profit = current_profit
            sell_day = i

    return buy_day, sell_day