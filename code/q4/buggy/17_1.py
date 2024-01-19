def max_profit(stock_prices):
    if not stock_prices or len(stock_prices) < 2:
        return []

    buy_day, sell_day = 0, 1  # Initialize buy and sell days
    min_price = stock_prices[0]  # Initialize the minimum price
    max_profit = stock_prices[sell_day] - min_price  # Initialize the maximum profit

    for i in range(1, len(stock_prices)):
        if stock_prices[i] < min_price:
            min_price = stock_prices[i]
            buy_day = i
        elif stock_prices[i] - min_price > max_profit:
            max_profit = stock_prices[i] - min_price
            sell_day = i

    return [buy_day, sell_day]