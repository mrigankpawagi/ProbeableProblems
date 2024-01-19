#write a function max_profit that takes a list with price per day and outputs the index of the best day to buy and sell. the dont need to be consecutive

def max_profit(prices):
  """
  This function finds the best day to buy and sell a stock based on a list of daily prices.

  Args:
    prices: A list of integers representing the price of the stock on each day.

  Returns:
    A tuple containing two integers: the index of the best day to buy and the index of the best day to sell.
  """

  # Initialize variables
  max_profit = 0
  buy_day = 0
  sell_day = 0

  # Loop through each day
  for i, price in enumerate(prices):
    # Check if buying on this day could lead to a higher profit
    for j in range(i + 1, len(prices)):
      current_profit = prices[j] - price
      if current_profit > max_profit:
        max_profit = current_profit
        buy_day = i
        sell_day = j

  # Return the buy and sell day indices
  return buy_day, sell_day