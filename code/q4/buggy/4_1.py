def max_profit(prices):
    if not prices or len(prices) < 2:
        # Return None for cases where there are not enough prices to analyze
        return None

    # Initialize variables to track the best buy and sell days
    buy_day = sell_day = 0
    max_profit = 0
    current_buy_day = 0

    for i in range(1, len(prices)):
        if prices[i] < prices[current_buy_day]:
            # Update the current buy day if a lower price is found
            current_buy_day = i
        elif prices[i] - prices[current_buy_day] > max_profit:
            # Update the sell day and max profit if a better selling opportunity is found
            buy_day = current_buy_day
            sell_day = i
            max_profit = prices[sell_day] - prices[buy_day]

    if max_profit == 0:
        # Return None if no profit can be made
        return None
    else:
        # Return the best buy and sell days
        return (buy_day, sell_day)