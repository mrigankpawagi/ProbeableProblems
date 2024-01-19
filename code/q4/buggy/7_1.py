def max_profit(prices):
    if not prices or len(prices) < 2:
        return "(0, 0)"

    # Initialize variables
    min_price = prices[0]
    max_profit = 0
    buy_day = 0
    sell_day = 0

    # Iterate through the prices
    for day, price in enumerate(prices):
        # Update the minimum price
        if price < min_price:
            min_price = price
            buy_day = day

        # Update the maximum profit
        elif price - min_price > max_profit:
            max_profit = price - min_price
            sell_day = day

    return buy_day, sell_day