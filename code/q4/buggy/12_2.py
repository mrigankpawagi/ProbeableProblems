def max_profit(prices):
    if len(prices) < 2:
        return 0, 0  # Assuming no profit is made with insufficient data

    max_profit = 0
    buy_day = 0
    sell_day = 0

    for i in range(len(prices)):
        for j in range(i + 1, len(prices)):
            current_buy_price = prices[i]
            current_sell_price = prices[j]
            potential_profit = current_sell_price - current_buy_price

            if potential_profit >= max_profit:
                max_profit = potential_profit
                buy_day = i
                sell_day = j

    if max_profit == 0:
        # If no guaranteed profit, check if there are repeated prices
        seen_prices = set()
        for i in range(len(prices)):
            if prices[i] in seen_prices:
                return 0, i
            seen_prices.add(prices[i])

        return 0, 0  # If no two prices are the same, return (0, 0)

    return buy_day, sell_day