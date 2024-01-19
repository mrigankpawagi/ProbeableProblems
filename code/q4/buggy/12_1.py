def max_profit(prices):
    if len(prices) < 2:
        return 0, 0  # Assuming no profit is made with insufficient data

    min_price = float('inf')  # Initialize min_price to positive infinity
    max_profit = 0
    buy_day = 0
    sell_day = 0

    for i in range(len(prices)):
        current_price = prices[i]

        if current_price < 0:
            continue  # Skip negative prices

        if current_price <= min_price:
            min_price = current_price
            buy_day = i

        potential_profit = current_price - min_price
        if potential_profit > max_profit:
            max_profit = potential_profit
            sell_day = i

    if max_profit == 0:
        # If no guaranteed profit, check if there are repeated prices
        seen_prices = set()
        for i in range(len(prices)):
            if prices[i] in seen_prices:
                return 0, i
            seen_prices.add(prices[i])

        return 0, 0  # If no two prices are the same, return (0, 0)

    return buy_day, sell_day