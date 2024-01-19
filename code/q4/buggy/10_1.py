def max_profit(price):
    # Handle the case where the input list is empty
    if not price:
        return None  # You may choose to return a specific value or raise an exception

    # Initialize variables to track the best days to buy and sell
    buy_day = 0
    sell_day = 0
    max_profit = 0

    # Iterate through the list to find the best days to buy and sell
    for i in range(len(price)):
        for j in range(i + 1, len(price)):
            profit = price[j] - price[i]
            if profit > max_profit:
                buy_day, sell_day = i, j
                max_profit = profit

    return (buy_day, sell_day)