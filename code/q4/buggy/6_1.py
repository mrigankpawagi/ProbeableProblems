def max_profit(prices):
    # Handle cases with insufficient data
    if not prices or len(prices) < 2:
        return "Not enough data to calculate profit"

    # Ignore negative and zero values
    filtered_prices = [(i, price) for i, price in enumerate(prices) if price > 0]

    if len(filtered_prices) < 2:
        return "Not enough positive data to calculate profit"

    max_profit = 0
    best_days = (0, 0)

    for i in range(len(filtered_prices)):
        for j in range(i+1, len(filtered_prices)):
            profit = filtered_prices[j][1] - filtered_prices[i][1]
            if profit > max_profit:
                max_profit = profit
                best_days = (filtered_prices[i][0], filtered_prices[j][0])

    return best_days if max_profit > 0 else "No profit possible"