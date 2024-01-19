def max_profit(prices):
  

    if len(prices) == 1:
        return f"Best day to buy: Day 1, Best day to sell: Day 1, Maximum Profit: 0"

    buy_day, sell_day = 0, 1
    max_profit = prices[sell_day] - prices[buy_day]

    if max_profit <= 0:
        return f"Best day to buy: Day 1, Best day to sell: Day 1, Maximum Profit: {max_profit}"

    for i in range(len(prices)):
        for j in range(i + 1, len(prices)):
            if prices[j] - prices[i] > max_profit:
                max_profit = prices[j] - prices[i]
                buy_day = i
                sell_day = j

    return f"Best day to buy: Day {buy_day + 1}, Best day to sell: Day {sell_day + 1}, Maximum Profit: {max_profit}"