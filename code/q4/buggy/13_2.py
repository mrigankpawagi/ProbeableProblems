def max_profit(price):
    if len(price) < 2:
        return None  # Cannot make a profit with less than two days of data

    buy_day = 0
    sell_day = 1
    min_price_index = 0
    max_profit = price[sell_day] - price[buy_day]

    for i in range(1, len(price)):
        if price[i] <= price[min_price_index]:
            min_price_index = i
        elif price[i] - price[min_price_index] > max_profit:
            buy_day = min_price_index
            sell_day = i
            max_profit = price[sell_day] - price[buy_day]

    return buy_day, sell_day