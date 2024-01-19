def max_profit(prices):
    min_price = float('inf')
    max_profit = 0
    buy_day = 0
    sell_day = 0

    for i in range(len(prices)):
        if prices[i] <= min_price:
            min_price = prices[i]
            buy_day = i
            sell_day = i
        elif prices[i] - min_price > max_profit:
            max_profit = prices[i] - min_price
            sell_day = i

    return buy_day, sell_day