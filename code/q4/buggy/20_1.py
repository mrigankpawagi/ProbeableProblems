def max_profit(prices):
    if len(prices) < 2:
        return (0, 0)  # Not enough data for buying and selling

    max_profit = 0
    buy_day, sell_day = 0, 0

    for i in range(len(prices)):
        if prices[i] <= 0:
            continue  # Skip invalid prices (0 and negative values)

        for j in range(i + 1, len(prices)):
            if prices[j] <= 0:
                continue  # Skip invalid prices (0 and negative values)

            profit = prices[j] - prices[i]
            if profit > max_profit:
                max_profit = profit
                buy_day, sell_day = i, j

    return (buy_day, sell_day) if max_profit > 0 else (0, 0)