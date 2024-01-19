def max_profit(prices):
    """
    Finds the best day to buy and sell a stock to maximize profit.

    Args:
        prices: A list of positive integers representing stock prices on different days.

    Returns:
        A tuple of two integers: (buy_day, sell_day) representing the best days to buy and sell.
    """

    if len(prices) < 2:
        return None 

    min_price = prices[0]
    max_profit = 0
    buy_day = 0
    sell_day = 0

    for i in range(1, len(prices)):
        current_price = prices[i]

     
        potential_profit = current_price - min_price

   
        if potential_profit > max_profit:
            max_profit = potential_profit
            buy_day = i - 1 
            sell_day = i

     
        min_price = min(min_price, current_price)

    return buy_day, sell_day