def max_profit(prices):
    if not prices or len(prices) < 2:
        return None  # Cannot make a profit with less than two prices

    buy_index, sell_index = 0, 1  # Initialize the buy and sell indices
    current_buy_index = 0  # Temporary buy index
    max_profit = prices[sell_index] - prices[buy_index]  # Initialize the maximum profit

    for i in range(1, len(prices)):
        current_profit = prices[i] - prices[current_buy_index]

        # Update the buy and sell indices if a higher profit is found
        if current_profit > max_profit:
            max_profit = current_profit
            buy_index = current_buy_index
            sell_index = i

        # Update the temporary buy index if a lower price is found
        if prices[i] < prices[current_buy_index]:
            current_buy_index = i

    return buy_index, sell_index