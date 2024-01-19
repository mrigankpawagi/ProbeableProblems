def max_profit(prices):
    if not prices or len(prices) < 2:
        return "Not enough data to calculate profit."

    # Initialize variables to track the minimum price and maximum profit
    min_price = prices[0]
    max_profit = 0
    buy_day = 0
    sell_day = 0

    # Iterate through the prices
    for day in range(1, len(prices)):
        current_price = prices[day]

        # Update the minimum price if a lower price is encountered
        if current_price < min_price:
            min_price = current_price
            buy_day = day

        # Update the maximum profit if a higher profit is found
        elif current_price - min_price > max_profit:
            max_profit = current_price - min_price
            sell_day = day

    return "Buy on day {} and sell on day {} for a maximum profit of {}".format(buy_day + 1, sell_day + 1, max_profit)