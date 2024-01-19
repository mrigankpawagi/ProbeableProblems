def max_profit(prices):
    if not prices or len(prices) < 2:
        return []  # Return an empty array if the list is empty or has less than two prices

    min_price = prices[0]
    max_profit_value = 0
    buy_time = 0
    sell_time = 0

    for i in range(1, len(prices)):
        current_price = prices[i]

        if current_price < min_price:
            min_price = current_price
            buy_time = i
        elif current_price - min_price > max_profit_value:
            max_profit_value = current_price - min_price
            sell_time = i

    return [buy_time, sell_time]