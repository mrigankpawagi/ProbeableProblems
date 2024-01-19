def max_profit(price):
 max_profit = 0
 buy_day = 0
 sell_day = 0

 # Loop through each day
 for i, p in enumerate(price):
   # Check if buying on this day could lead to a higher profit
   for j in range(i + 1, len(price)):
     current_profit = price[j] - p
     if current_profit > max_profit:
       max_profit = current_profit
       buy_day = i
       sell_day = j

 # Return the buy and sell day indices
 return buy_day, sell_day