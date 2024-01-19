def max_profit(prices):
    if not prices or len(prices) < 2:
        return "Not enough data to calculate profit"

    max_profit = 0
    buy_day = 0
    sell_day = 0

    for i in range(len(prices) - 1):
        for j in range(i + 1, len(prices)):
            profit = prices[j] - prices[i]
            if profit > max_profit:
                max_profit = profit
                buy_day = i + 1
                sell_day = j + 1

    return f"Buy on day {buy_day} and sell on day {sell_day} for a maximum profit of {max_profit}"