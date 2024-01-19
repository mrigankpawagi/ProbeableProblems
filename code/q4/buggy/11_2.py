def max_profit(price):
    if not price or len(price) < 2:
        return [0,0]

    buy_day = 0
    sell_day = 0
    max_profit = 0

    for i in range(len(price)):
        for j in range(i + 1, len(price)):
            if price[j] - price[i] > 0 and price[j] - price[i] >= max_profit:
                max_profit = price[j] - price[i]
                buy_day = i
                sell_day = j

    return [buy_day, sell_day] if max_profit > 0 else [0,0]